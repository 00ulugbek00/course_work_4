import requests

from API.base_api import BaseParser
from models.vacancy import Vacancy
from utils.currency_converter import get_currency_data


class HeadHunterAPI(BaseParser):
    def __init__(self, url: str, job_title: str):
        """
        Инициализация класса HeadHunterAPI
        """

        super().__init__(url, job_title)
        self._params = {
            'text': job_title,
            'per_page': 100,
            'only_with_salary': True
        }

    def get_from_api(self):
        """
        Метод для загрузки данных с внешнего API
        :return: вовращает данные по API в виде словаря json
        """
        response = requests.get(self._url, params=self._params)
        result = response.json().get("items", [])
        return self._create_models(result)

    def __repr__(self):
        return f"HeadHunterAPI ({self._url})"

    def _create_models(self, data: list):
        """
        Метод для создания списка экземляров класса
        """
        vacancies = []
        for item in data:
            try:
                if item['salary']['from']:
                    if item['salary']['currency'].upper() not in ["RUR", "RUB"]:
                        item['salary']['from'] *= get_currency_data(item['salary']['currency'])

                    vacancy = Vacancy(id=item['id'], title=item['name'], url=item['alternate_url'],
                                      payment_from=int(item['salary']['from']),
                                      city=item['area']['name'])
                    if self._job_title.lower() in item['name'].lower():
                        vacancies.append(vacancy)
            except Exception as e:
                print(f"Возникла ошибка {e}")

        return vacancies
