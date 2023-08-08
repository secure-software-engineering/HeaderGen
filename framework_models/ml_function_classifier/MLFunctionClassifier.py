import os
import pickle

import numpy as np

from framework_models.ml_function_classifier.data_cleaning import data_cleaning

script_dir = os.path.abspath(os.path.dirname(__file__))


class MLFunctionClassifier:
    def __init__(self):
        with open(f"{script_dir}/highlevel_vectorizer.pkl", "rb") as f:
            self.highlevel_vectorizer = pickle.load(f)

        with open(f"{script_dir}/highlevel_classifier.pkl", "rb") as f:
            self.highlevel_classifier = pickle.load(f)

        with open(f"{script_dir}/dp_vectorizer.pkl", "rb") as f:
            self.dp_vectorizer = pickle.load(f)

        with open(f"{script_dir}/dp_classifier.pkl", "rb") as f:
            self.dp_classifier = pickle.load(f)

        with open(f"{script_dir}/fe_vectorizer.pkl", "rb") as f:
            self.fe_vectorizer = pickle.load(f)

        with open(f"{script_dir}/fe_classifier.pkl", "rb") as f:
            self.fe_classifier = pickle.load(f)

        with open(f"{script_dir}/mb_vectorizer.pkl", "rb") as f:
            self.mb_vectorizer = pickle.load(f)

        with open(f"{script_dir}/mb_classifier.pkl", "rb") as f:
            self.mb_classifier = pickle.load(f)

        self.dp_labels = [
            "Data Cleaning Filtering",
            "Data Loading",
            "Data Preparation and Exploration",
            "Data Sub-sampling and Train-test Splitting",
            "Exploratory Data Analysis",
        ]

        self.fe_labels = [
            "Feature Engineering",
            "Feature Selection",
            "Feature Transformation",
        ]

        self.mb_labels = [
            "Model Building and Training",
            "Model Parameter Tuning",
            "Model Training",
            "Model Validation and Assembling",
        ]

    def predict_dp(self, preprocessed_docstring):
        dp_numerical_vector = self.dp_vectorizer.transform([preprocessed_docstring])
        dp_predicted_probabilities = self.dp_classifier.predict_proba(
            dp_numerical_vector
        )
        dp_predicted_label = (dp_predicted_probabilities > 0.5).astype(int)
        dp_indices = np.where(np.array(dp_predicted_label) == 1)[1]
        dp_predicted_classes = [self.dp_labels[i] for i in dp_indices]
        return dp_predicted_classes

    def predict_fe(self, preprocessed_docstring):
        fe_numerical_vector = self.fe_vectorizer.transform([preprocessed_docstring])
        fe_predicted_probabilities = self.fe_classifier.predict_proba(
            fe_numerical_vector
        )
        fe_predicted_label = (fe_predicted_probabilities > 0.5).astype(int)
        fe_indices = np.where(np.array(fe_predicted_label) == 1)[1]
        fe_predicted_classes = [self.fe_labels[i] for i in fe_indices]
        return fe_predicted_classes

    def predict_mb(self, preprocessed_docstring):
        mb_numerical_vector = self.mb_vectorizer.transform([preprocessed_docstring])
        mb_predicted_probabilities = self.mb_classifier.predict_proba(
            mb_numerical_vector
        )
        mb_predicted_label = (mb_predicted_probabilities > 0.5).astype(int)
        mb_indices = np.where(np.array(mb_predicted_label) == 1)[1]
        mb_predicted_classes = [self.mb_labels[i] for i in mb_indices]
        return mb_predicted_classes

    def predict_function(self, func_call, docstring):
        root = func_call.split(".")[0]
        if root in ["warnings", "os", "posix"]:
            return []

        preprocessed_docstring = data_cleaning(docstring)
        if len(preprocessed_docstring.split()) < 5:
            return []

        highlevel_numerical_vector = self.highlevel_vectorizer.transform(
            [preprocessed_docstring]
        )
        highlevel_predicted_probabilities = self.highlevel_classifier.predict_proba(
            highlevel_numerical_vector
        )
        highlevel_predicted_label = (highlevel_predicted_probabilities > 0.5).astype(
            int
        )
        if (
            highlevel_predicted_probabilities[0][0] > 0.5
            and highlevel_predicted_probabilities[0][1] > 0.3
        ):
            highlevel_predicted_label[0][1] = 1

        predicted_classes = []

        if highlevel_predicted_label[0][0] == 1:
            dp_classes = self.predict_dp(preprocessed_docstring)

            if len(dp_classes) == 1:
                predicted_classes.extend(dp_classes)
            else:
                predicted_classes.append("Data Preparation and Exploration")

        if highlevel_predicted_label[0][1] == 1:
            fe_classes = self.predict_fe(preprocessed_docstring)
            if len(fe_classes) == 1:
                predicted_classes.extend(fe_classes)
            else:
                predicted_classes.append("Feature Engineering")

        if highlevel_predicted_label[0][2] == 1:
            mb_classes = self.predict_mb(preprocessed_docstring)
            if len(mb_classes) == 1:
                predicted_classes.extend(mb_classes)
            else:
                predicted_classes.append("Model Building and Training")

        if highlevel_predicted_label[0][3] == 1:
            predicted_classes.append("Visualization")

        return predicted_classes
