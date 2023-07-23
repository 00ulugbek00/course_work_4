from abc import ABC, abstractmethod
from models.vacancy import Vacancy


class BaseStorage(ABC):

    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def write(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def read(self):
        pass
