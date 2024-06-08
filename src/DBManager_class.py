import psycopg2
from utils.config import config


class DBManager:
    """
     класс DBManager будет подключаться
     к БД PostgreSQL и использовать нижеследующие
     методы для выполнения запросов пользователя
    """
    def __init__(self, db_name):
        """
                инициализируем класс
        :param db_name: имя БД, с которой будет работать экземпляр класса
        """
        self.__db_name = db_name

    def __execute_query(self, query, params=None):
        """
                метод, позволяюций получать ответ
                на запрос пользователя
        :param query: запрос, который передается
        :param params: параметр, который можно передать в запрос
        :return: результат запроса
        """
        conn = psycopg2.connect(dbname=self.__db_name, **config())
        with conn:
            with conn.cursor() as cur:
                if params:
                    cur.execute(query, params)
                else:
                    cur.execute(query)
                result = cur.fetchall()
        conn.close()
        return result

    def get_companies_and_vacancies_count(self):
        """
                получает список всех компаний
                и количество вакансий у каждой компании

        :return: результат запроса
        """
        query = "SELECT name, open_vacancies FROM employers "
        result = self.__execute_query(query)
        data = [{'company_name': row[0], 'vacancies_count': row[1]} for row in result]
        return data

    def get_all_vacancies(self):
        """
                получает список всех вакансий
                с указанием названия компании,
                названия вакансии, зарплаты
                и ссылки на вакансию

        :return: результат запроса
        """
        query = "SELECT employers.name, vacancies.id, vacancies.name, vacancies.alternate_url, \
                salary_from, salary_to  FROM vacancies " \
                "JOIN employers ON vacancies.employer_id = employers.id " \
                "ORDER BY employers.name ASC"
        result = self.__execute_query(query)
        data = [{'company_name': row[0], 'vacancy_id': row[1],
                 'vacancy_name': row[2], 'vacancy_url': row[3],
                 'salary_from': row[4], 'salary_to': row[5]} for row in result]
        return data

    def get_avg_salary(self):
        """
                получает среднюю зарплату по вакансиям

        :return:результат запроса
        """
        query = "SELECT AVG(salary_from) FROM vacancies "
        result = self.__execute_query(query)
        data = [{'avg_salary': row[0]} for row in result]
        return data

    def get_vacancies_with_higher_salary(self):
        """
                получает список всех вакансий,
                у которых зарплата выше средней
                по всем вакансиям

        :return: результат запроса
        """
        query = "SELECT employers.name, vacancies.id, vacancies.name, vacancies.alternate_url, \
                salary_from, salary_to  FROM vacancies " \
                "INNER JOIN employers ON vacancies.employer_id = employers.id " \
                "WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)" \
                "ORDER BY salary_from"
        result = self.__execute_query(query)
        data = [{'company_name': row[0], 'vacancy_id': row[1],
                 'vacancy_name': row[2], 'vacancy_url': row[3],
                 'salary_from': row[4], 'salary_to': row[5]} for row in result]
        return data

    def get_vacancies_with_keyword(self):
        """
                получает список всех вакансий,
                в названии которых содержатся
                переданные в метод слова,
                например python.

        :return: результат запроса с ключевым словом

        """
        key_word = input("Введите ключевое слово для поиска вакансий: \n").lower()
        updated_key_word = f"%{key_word}%"
        query = "SELECT employers.name, vacancies.id, vacancies.name, vacancies.alternate_url, \
                salary_from, salary_to  FROM vacancies " \
                "INNER JOIN employers ON vacancies.employer_id = employers.id " \
                "WHERE LOWER(vacancies.name) LIKE %s" \
                "ORDER BY employers.name, salary_from DESC"
        result = self.__execute_query(query, (updated_key_word,))
        data = [{'company_name': row[0], 'vacancy_id': row[1],
                 'vacancy_name': row[2], 'vacancy_url': row[3],
                 'salary_from': row[4], 'salary_to': row[5]} for row in result]
        return data
