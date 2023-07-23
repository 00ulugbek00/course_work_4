from API.HanterApi import HeadHunterAPI
from API.job_file import SuperJobAPI
from file_handler.storage_json import FileStorageJSON
from pprint import pprint


class VacancyService:
    def __init__(self, hh_file: HeadHunterAPI, superjob_file: SuperJobAPI, filestorage: FileStorageJSON):
        """
        Инициализация класса VacancyService

        :param hh: экземпляр класса HeadHunterAPI.
        :param superjob: экземпляр класса SuperJobAPI.
        :param filestorage: экземпляр класса FileStorage
        """
        self._hh_file = hh_file
        self._superjob_file = superjob_file
        self._filestorage = filestorage
        self._hh_vacancies = []
        self._superjob_vacancies = []
        self._all_vacancies = []
        self.__main_menu()

    def __main_menu(self):
        while True:
            command = input("Чтобы получить список всех вакансий введите '1'  \n"
                            "Чтобы получить список top 10 вакансий введите '2' \n"
                            "Чтобы получить список вакансий c максимальной зарплатой введите '3'\n"
                            "Чтобы получить список вакансий c минимальной зарплатой введите '4' \n"
                            "Чтобы записать список вакансии в файл введите '5' \n"
                            "Чтобы выгрузить список вакансий из файла '6' \n"
                            "Выход из программы '0'\n")
            if command == "1":
                self.__output_all_vacancies()
                print("Вакансии загружено успешно")
            elif command == "2":
                top = input("Сколько вакансий хотите получить: ")
                self.__ouput_top_vacancies(int(top))
            elif command == "3":
                self.__output_max_salary()
            elif command == "4":
                self.__output_min_salary()
            elif command == "5":
                self.__save_to_json()
                print("Вакансии сохранены успешно")
            elif command == "6":
                vacancies = self.__get_from_json()
                pprint(vacancies)
            elif command == "0":
                print("Завершение программы")
                exit()
            else:
                print("Неизвестная команда")

    def __output_all_vacancies(self):
        """
        Метод получает все вакансии из API HeadHunter и SuperJob.

        :return: - list: список словарей, представляющих вакансии.
        """
        self._hh_vacancies.extend(self._hh_file.get_from_api())
        self._superjob_vacancies.extend(self._superjob_file.get_from_api())
        self._all_vacancies = self._hh_vacancies + self._superjob_vacancies
        [print(vacancy) for vacancy in self._all_vacancies]

    def __ouput_top_vacancies(self, count: int = 10):
        """
        Метод получает топ N вакансий на основе их рейтинга
        :param count: количество топовых вакансий для получения. По умолчанию 10
        :return: список словарей, представляющих топовые вакансии

        """
        vacancies_sorted = sorted(self._all_vacancies, reverse=True)[:count]
        [print(vacancy) for vacancy in vacancies_sorted]

    def __output_max_salary(self):
        """
        Метод получает вакансию с наивысшей зарплатой

        :return:объект вакансии с наивысшей зарплатой
        """
        print(max(self._all_vacancies))

    def __output_min_salary(self):
        """
        Метод получает вакансию с наименьшей зарплатой
        :return: объект вакансии с наименьшей зарплатой
        """
        print(min(self._all_vacancies))

    def __save_to_json(self):
        """
        Cохраняет все вакансии в JSON-файл с использованием хранилища файлов
        """
        [self._filestorage.write(vacancy) for vacancy in self._all_vacancies]

    def __get_from_json(self):
        """
        Метод получает все вакансии из JSON-файла с использованием хранилища файлов
        """
        return self._filestorage.read()
