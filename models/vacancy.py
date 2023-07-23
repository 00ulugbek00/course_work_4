from functools import total_ordering


@total_ordering
class Vacancy:
    def __init__(self, id: int, title: str, url: str, payment_from: int, city: str):
        self.id = id
        self.title = title
        self.url = url
        self.payment_from = payment_from
        self.city = city

    def __str__(self):
        return f"Id вакансии: {self.id}\nНазвание: {self.title}\nСсылка: {self.url}\nЗарплата: {self.payment_from} рублей\nГород: {self.city}\n"

    def __eq__(self, other):
        return self.payment_from == other.payment_from

    def __lt__(self, other):
        return self.payment_from < other.payment_from
