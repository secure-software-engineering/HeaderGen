from abc import ABCMeta, abstractmethod

class BaseLink(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, y_pred): ...
    @abstractmethod
    def derivative(self, y_pred): ...
    @abstractmethod
    def inverse(self, lin_pred): ...
    @abstractmethod
    def inverse_derivative(self, lin_pred): ...

class IdentityLink(BaseLink):
    def __call__(self, y_pred): ...
    def derivative(self, y_pred): ...
    def inverse(self, lin_pred): ...
    def inverse_derivative(self, lin_pred): ...

class LogLink(BaseLink):
    def __call__(self, y_pred): ...
    def derivative(self, y_pred): ...
    def inverse(self, lin_pred): ...
    def inverse_derivative(self, lin_pred): ...

class LogitLink(BaseLink):
    def __call__(self, y_pred): ...
    def derivative(self, y_pred): ...
    def inverse(self, lin_pred): ...
    def inverse_derivative(self, lin_pred): ...
