import requests

from contact import SUPERJOB_CODE
from API.base_api import BaseParser
from models.vacancy import Vacancy
from utils.currency_converter import get_currency_data


class SuperJobAPI(BaseParser):
    def __init__(self, url: str, job_title: str):
        """
        Инициализация класса SuperJobAPI
        """

        super().__init__(url, job_title)

        self._params = {"keywords": [[1, job_title]],
                        "count": 100,
                        }

        self._headers = {
            'X-Api-App-Id': SUPERJOB_CODE,
        }

    def get_from_api(self):
        """
        Метод для загрузки данных с внешнего API
        :return: вовращает данные по API в виде словаря json
        """

        response = requests.get(self._url, headers=self._headers, params=self._params)
        result = response.json().get("objects", [])

        return self._create_models(result)

    def _create_models(self, data: list):
        """
        Метод для создания списка экземляров класса
        """
        vacancies = []
        for item in data:
            if int(item['payment_from']) != 0:
                if item['currency'].upper() not in ["RUR", "RUB"]:
                    item['payment_from'] *= get_currency_data(item['currency'])
                vacancy = Vacancy(id=int(item['id']), title=item['profession'], url=item['link'],
                                  payment_from=int(item['payment_from'])
                                  , city=item['town']['title'])
                if self._job_title.lower() in item['profession'].lower():
                    vacancies.append(vacancy)
        return vacancies
