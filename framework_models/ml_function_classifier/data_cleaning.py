import re

import nltk

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))


def clean_dataframe_text(text):
    # remove pd.DataFrame()
    pattern = r"df\s*=\s*pd\.DataFrame\(((?:\([^()]*\)|[^()])*)\)"
    cleaned_text = re.sub(pattern, "", text, flags=re.DOTALL)

    pattern = r"^\s*df\s*=\s*pd\.DataFrame\({.*},?\s*index=\[.*\]\)\s*$"
    cleaned_text = re.sub(pattern, "", cleaned_text, flags=re.DOTALL)

    # remove >>df and its next line
    pattern = r"^>>> df\s*$\n^.*$\n"
    cleaned_text = re.sub(pattern, "", cleaned_text, flags=re.MULTILINE)

    # 0  Yum Yum   cup     4.0
    pattern = r"^\d+\s+.*$[\n\r]*?"
    cleaned_text = re.sub(pattern, "", cleaned_text, flags=re.MULTILINE)

    # Portland    17.0    62.6

    pattern = r"\n([A-Z][a-z]+)\s+\d+\.\d+(\s+\d+\.\d+){0,2}"
    cleaned_text = re.sub(pattern, "", cleaned_text)

    return cleaned_text.strip()


def remove_latex(text):
    # Remove code blocks starting with `.. math::`
    text = re.sub(
        r"^\s*\.\.\s*math::\n\s*(.*?)\n(\n|$)",
        " ",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )

    # remove include statements

    text = re.sub(r"^\s*..\s+include::\s+.+", " ", text, flags=re.MULTILINE)

    # remove the version added statements such as .. versionadded:: 0.19

    text = re.sub(r"^\s*\.\. versionadded:: .*$", "", text, flags=re.MULTILINE)

    # remove the deprecated statements such as .. deprecated::

    text = re.sub(r"^\s*\.\. deprecated:: .*$", "", text, flags=re.MULTILINE)

    return text


def remove_math_words(text):
    # remove words that starts with :math:`sometext`
    return re.sub(r":math:`[^`]*`", "", text)


def remove_urls(text):
    # remove the urls starts with https:
    return re.sub(r"http\S+", " ", text)


def remove_references(text):
    # References ...
    text = re.sub(r"References\s+-+\s+[\s\S]*", "", text)

    #:ref:``
    text = re.sub(r":ref:`[^`]*`", "", text)

    return text


def remove_single_letter_underscore(text):
    # remove the underscore letters with single letter on each sides such as  h_0, c_0
    pattern = r"\b\w{0,1}_\w{0,1}\b"
    return re.sub(pattern, " ", text)


def remove_non_alpha(text):
    # remove non alpha characters
    cleaned_text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return cleaned_text


def remove_single_letters(text):
    # Remove single letters such as h ,k i
    return re.sub(r"(?<!\S)\w(?!\S)", " ", text)


def remove_stopwords_and_lemmatize(text):
    # remove stop words and lemmatize the text
    word_tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    filtered_text = [
        lemmatizer.lemmatize(word)
        for word in word_tokens
        if not word.lower() in stop_words
    ]
    return " ".join(filtered_text).lower()


def data_cleaning(text):
    cleanedtext = remove_latex(text)
    cleanedtext = clean_dataframe_text(cleanedtext)
    cleanedtext = remove_urls(cleanedtext)
    cleanedtext = remove_math_words(cleanedtext)
    cleanedtext = remove_references(cleanedtext)
    cleanedtext = remove_single_letter_underscore(cleanedtext)
    cleanedtext = remove_non_alpha(cleanedtext)
    cleanedtext = remove_single_letters(cleanedtext)
    cleanedtext = remove_stopwords_and_lemmatize(cleanedtext)
    return cleanedtext
