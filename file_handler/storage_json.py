import json

from file_handler.base_storage import BaseStorage
from models.vacancy import Vacancy


class FileStorageJSON(BaseStorage):
    def __init__(self, filename: str):
        """
       Инициализация класса FileStorage
       """
        self._filename = filename

    def write(self, vacancy: Vacancy):
        """
        Метод для записи файла

        """

        with open(self._filename, 'a', encoding='utf-8') as file:
            vacancy_dict = {
                "id": vacancy.id,
                "title": vacancy.title,
                "link": vacancy.url,
                "salary": vacancy.payment_from,
                "city": vacancy.city
            }
            json.dump(vacancy_dict, file, ensure_ascii=False)
            file.write("\n")

    def read(self):
        """
        Метод для чтения файла

        """
        try:
            with open(self._filename, 'r', encoding='utf-8') as file:
                data = [json.loads(line) for line in file]
                return data
        except FileNotFoundError:
            # Если файл не найден, вернуть пустой список.
            return []
