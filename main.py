from utils.db_utils import create_database, create_tables, insert_data_in_tables, drop_db
from src.DBManager_class import DBManager

# db_name = "coursework"
# create_database(db_name)
# create_tables(db_name)
# insert_data_in_tables(db_name)
#
# db = DBManager("coursework")
# print(db.get_companies_and_vacancies_count())
# print(db.get_all_vacancies())
# print(db.get_avg_salary())
# print(db.get_vacancies_with_higher_salary())
# print(db.get_vacancies_with_keyword())


def display_data(data, headers, widths):
    header_line = " | ".join(header.ljust(width) for header, width in zip(headers, widths))
    print(header_line)
    print("-" * sum(widths))
    for item in data:
        line = " | ".join(str(item[header]).ljust(width) for header, width in zip(headers, widths))
        print(line)


def user_interactions():
    """
        Интерактив с пользователем:

    :return:
    """
    # 1 — Получаем от пользователя название БД
    db_name = input("Введите название своей базы данных: \n")

    # 2 — Создаем БД с названием пользователя
    create_database(db_name)

    # 3 — Создаем таблицы в БД
    create_tables(db_name)

    # 4 — Вставляем данные в таблицу
    insert_data_in_tables(db_name)

    # 5 — Создаем экземпляр БД для работы с методами
    db = DBManager(db_name)

    # Черновой

    # if method_num == 1:
    #     data = db.get_companies_and_vacancies_count()
    #     print("Вот, что мы наколдовали!\n")
    #     print("Компания                  | Количество вакансий")
    #     print("-" * 50)
    #     for item in data:
    #         print(f"{item['company_name'].ljust(25)} | {str(item['vacancies_count']).rjust(20)}")
    #     drop_db(db_name)
    #
    # elif method_num == 2:
    #     data = db.get_all_vacancies()
    #     print("Вот, что мы наколдовали!\n")
    #     print("Компания                       | ID вакансии | Вакансия                 "
    #           "                                                                    |"
    #           " Ссылка                          |  ЗП от  | ЗП до   ")
    #     print("-" * 200)
    #     for item in data:
    #         print(
    #             f"{item['company_name'].ljust(30)} | {str(item['vacancy_id']).ljust(11)} | "
    #             f"{item['vacancy_name'].ljust(92)} | {item['vacancy_url']} | "
    #             f"{str(item['salary_from']).ljust(7)} | {str(item['salary_to']).ljust(7)}")
    #     drop_db(db_name)
    #
    # elif method_num == 3:
    #     data = db.get_avg_salary()
    #     print("Вот, что мы наколдовали!\n")
    #     print("Средняя ЗП по вакансиям ")
    #     print("-" * 25)
    #     for item in data:
    #         print(f"{item['avg_salary']}")
    #     drop_db(db_name)
    #
    # elif method_num == 4:
    #     data = db.get_vacancies_with_higher_salary()
    #     print("Вот, что мы наколдовали!\n")
    #     print("Компания                       | ID вакансии | Вакансия                 "
    #           "                                           |"
    #           " Ссылка                          |  ЗП от  | ЗП до   ")
    #     print("-" * 200)
    #     for item in data:
    #         print(
    #             f"{item['company_name'].ljust(30)} | {str(item['vacancy_id']).ljust(11)} | "
    #             f"{item['vacancy_name'].ljust(67)} | {item['vacancy_url']} | "
    #             f"{str(item['salary_from']).ljust(7)} | {str(item['salary_to']).ljust(7)}")
    #     drop_db(db_name)
    #
    # elif method_num == 5:
    #     data = db.get_vacancies_with_keyword()
    #     print("Вот, что мы наколдовали!\n")
    #     print("Компания                       | ID вакансии | Вакансия                 "
    #           "                                           |"
    #           " Ссылка                          |  ЗП от  | ЗП до   ")
    #     print("-" * 200)
    #     for item in data:
    #         print(
    #             f"{item['company_name'].ljust(30)} | {str(item['vacancy_id']).ljust(11)} | "
    #             f"{item['vacancy_name'].ljust(67)} | {item['vacancy_url']} | "
    #             f"{str(item['salary_from']).ljust(7)} | {str(item['salary_to']).ljust(7)}")
    #     drop_db(db_name)
    #
    # # 8 — Если пользователь вводит что-то иное, удаляем бд,
    # # которую создали, и начинаем заново
    # else:
    #     print("Что-то пошло не так.\n "
    #           "Нужно ввести число от 1 до 5.\n "
    #           "Попробуй снова!\n")
    #     drop_db(db_name)
    #     user_interactions()

    methods = {
        1: {
            'function': db.get_companies_and_vacancies_count,
            'headers': ["company_name", "vacancies_count"],
            'widths': [30, 20]
        },
        2: {
            'function': db.get_all_vacancies,
            'headers': ["company_name", "vacancy_id", "vacancy_name", "vacancy_url", "salary_from", "salary_to"],
            'widths': [30, 11, 40, 60, 7, 7]
        },
        3: {
            'function': db.get_avg_salary,
            'headers': ["avg_salary"],
            'widths': [25]
        },
        4: {
            'function': db.get_vacancies_with_higher_salary,
            'headers': ["company_name", "vacancy_id", "vacancy_name", "vacancy_url", "salary_from", "salary_to"],
            'widths': [30, 11, 40, 60, 7, 7]
        },
        5: {
            'function': db.get_vacancies_with_keyword,
            'headers': ["company_name", "vacancy_id", "vacancy_name", "vacancy_url", "salary_from", "salary_to"],
            'widths': [30, 11, 40, 60, 7, 7]
        }
    }
    # 6 — Узнаем у пользователя, какой метод он хотел бы использовать
    while True:
        try:
            method_num = int(input("\nВы можете: \n"
                                   "[1] — получить список всех компаний и количество вакансий у каждой компании \n"
                                   "[2] — получить список всех вакансий с указанием названия компании, "
                                   "названия вакансии и зарплаты и ссылки на вакансию \n"
                                   "[3] — получить среднюю зарплату по вакансиям \n"
                                   "[4] — получить список всех вакансий, у которых зарплата"
                                   " выше средней по всем вакансиям \n"
                                   "[5] — получить список всех вакансий, "
                                   "в названии которых содержится переданное в метод слово \n"
                                   "[6] — выйти\n"))

            # 7 — Смотрим, что выбрал пользователь, и действуем исходя из заданного
            if method_num == 6:
                print("Уже уходите? Спасибо, что протестировали эту программу :)\n"
                      "Пока ищем портал для выхода...\n"
                      "А вот и выход...")
                break

            if method_num in methods:
                method = methods[method_num]
                data = method['function']()
                print("Вот, что мы наколдовали!\n")
                display_data(data, method['headers'], method['widths'])
            else:
                print("Что-то пошло не так. Нужно ввести число от 1 до 6.")
        except ValueError:
            print("Пожалуйста, введите корректное число от 1 до 6.")

    # 8 — Удаляем БД
    drop_db(db_name)


if __name__ == "__main__":
    print("Привет! Да начнутся наши поиски! :)")
    user_interactions()
