import requests

url_response = "https://api.hh.ru/employers/"
url_vacancies = "https://api.hh.ru/vacancies/"
# https://api.hh.ru/employers/{employer_id}")
# https://api.hh.ru/vacancies/


class ConnectAPI:

    @staticmethod
    def __get_response():
        """
                Умеет подключаться к API и
                получать данные о компании
                и её вакансиях
        """
        params = {"sort_by": "by_vacancies_open", "per_page": 10}
        response = requests.get("https://api.hh.ru/employers", params=params)
        response_dict = response.json()
        if response.status_code == 200:
            return response_dict['items']

    def get_employers(self):
        """
                Получаем данные о работодателях
                через итерации:
                - id работодателя,
                - наименование работодателя,
                - число открытых вакансий,
                - ссылка на работодателя
        :return:
        """
        data = self.__get_response()
        employers = []
        for employer in data:
            employers.append({"id": employer["id"], "name": employer["name"],
                              "open_vacancies": employer["open_vacancies"],
                              "alternate_url": employer["alternate_url"]})
        return employers

    def get_vacancies(self):
        """
                Получаем отфильтрованные через
                static method __filter_vacancies
                данные об открытых вакансиях
                работодателей через итерации,
                добавляя их в список вакансий
        :return:
        """
        employers = self.get_employers()
        vacancies = []
        for employer in employers:
            params = {"employer_id": employer["id"]}
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            if response.status_code == 200:
                filtered_vacancies = self.__filter_vacancies(response.json()['items'])
                vacancies.extend(filtered_vacancies)
        return vacancies

    @staticmethod
    def __filter_vacancies(vacancies):
        """

        :param vacancies:
        :return:
        """
        filtered_vacancies = []
        for vacancy in vacancies:
            if vacancy["salary"] is None:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            filtered_vacancies.append({
                "id": vacancy["id"],
                "name": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "employer": vacancy["employer"]["id"]
            })
        return filtered_vacancies


# hh = ConnectAPI()
# print(hh.get_employers())
# print(hh.get_vacancies())
# print(len(hh.get_vacancies()))
