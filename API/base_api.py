from abc import ABC, abstractmethod


class BaseParser(ABC):
    @abstractmethod
    def __init__(self, url: str, job_title: str):
        self._url = url
        self._job_title = job_title

    @abstractmethod
    def get_from_api(self):
        pass

