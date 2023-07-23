from contact import HH_URL, SUPERJOB_URL, DATA_FILE
from API.HanterApi import HeadHunterAPI
from API.job_file import SuperJobAPI
from app.JobSearchApp import VacancyService
from file_handler.storage_json import FileStorageJSON

vacancy_name = str(input("Введите название вакансии: "))
hh_api = HeadHunterAPI(HH_URL, vacancy_name)
sj_api = SuperJobAPI(SUPERJOB_URL, vacancy_name)
json_storage = FileStorageJSON(DATA_FILE)

VacancyService(hh_api, sj_api, json_storage)
