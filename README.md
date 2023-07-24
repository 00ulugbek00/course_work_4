[![trophy](https://github-profile-trophy.vercel.app/?username=ryo-ma)](https://github.com/ryo-ma/github-profile-trophy)
[![KnlnKS's LeetCode stats](https://leetcode-stats-six.vercel.app/api?username=KnlnKS)](https://github.com/00ulugbek00/leetcode-stats)
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?00ulugbek00r=DenverCoder1)](https://git.io/streak-stats)

course_work_4

Job Searсh
Проект "Job Search App" представляет собой приложение для поиска и обработки вакансий из различных API. Пользователь может выполнять поиск вакансий, отображать результаты, сохранять вакансии в файлы.

Установка
Для установки проекта вам потребуется выполнить следующие шаги:

Склонируйте репозиторий с помощью команды:
   git clone https://github.com/00ulugbek/course_work_4.git
Перейдите в папку проекта:
    cd course_work_4
Установите необходимые зависимости, выполнив команду (для работы приложения требуется python >= 3.11):
    pip install -r requirements.txt
Использование
Для запуска приложения выполните следующую команду:

    python main.py
После запуска приложения вы увидите меню с доступными действиями:

Поиск вакансий: Выполняет поиск вакансий по заданной должности.
Отобразить вакансии: Отображает найденные вакансии.
Сохранить вакансии в файл: Сохраняет найденные вакансии в файлы JSON и CSV.
Выход: Завершает работу приложения.
Функциональность
Класс JobSearchApp
Класс JobSearchApp представляет основное приложение для выполнения операций по поиску и обработке вакансий.

Методы класса
__init__(self): Инициализирует объект JobSearchApp.
__vacancy(self): Выполняет поиск вакансий.
_self.__output_all_vacancies(vacancy): Получает название вакансии.
__(vacancy): Получает ссылку на вакансию.
____output_max_salary(vacancy): Получает зарплату от вакансии.
__get_currency(vacancy): Получает валюту вакансии.
__check_currency(title, link, salary, date, currency): Проверяет валюту и преобразует зарплату.
__ouput_top_vacancies__save_vacancies_to_files(self): Сохраняет вакансии в файлы JSON и CSV. 
course_work_4/README.md at main · course_work_4
