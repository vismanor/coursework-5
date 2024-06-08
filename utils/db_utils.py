import psycopg2
from utils.config import config
from src.api_connect_class import ConnectAPI


def create_database(db_name):
    """
            Создает БД
    :param db_name:
    :return:
    """
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'''DROP DATABASE IF EXISTS {db_name}''')
    cur.execute(f'''CREATE DATABASE {db_name}''')
    cur.close()
    conn.close()


def create_tables(db_name):
    """
            Создает таблицы в БД
    :param db_name:
    :return:
    """
    conn = psycopg2.connect(dbname=db_name, **config())
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE employers"
                        "(id INTEGER PRIMARY KEY, "
                        "name VARCHAR (150), "
                        "open_vacancies INTEGER, "
                        "alternate_url VARCHAR (150))")
            cur.execute("CREATE TABLE vacancies "
                        "(id INTEGER PRIMARY KEY, "
                        "name VARCHAR (150), "
                        "alternate_url VARCHAR (150), "
                        "salary_from INTEGER, "
                        "salary_to INTEGER, "
                        "employer_id INTEGER REFERENCES employers(id))")
    conn.close()


def insert_data_in_tables(db_name):
    """
            Вставляет полученные данные в таблицы БД
    :param db_name:
    :return:
    """
    hh = ConnectAPI()
    employers = hh.get_employers()
    vacancies = hh.get_vacancies()
    conn = psycopg2.connect(dbname=db_name, **config())
    with conn:
        with conn.cursor() as cur:
            for employer in employers:
                cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s)",
                            (employer["id"], employer["name"],
                             employer["open_vacancies"],
                             employer["alternate_url"]))
            for vacancy in vacancies:
                cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)",
                            (vacancy["id"], vacancy["name"],
                             vacancy["url"], vacancy["salary_from"],
                             vacancy["salary_to"], vacancy["employer"]))
    conn.close()


def drop_db(db_name):
    """
        Удаляет БД по окончании интеркатива с пользователем
    :param db_name:
    :return:
    """
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'''DROP DATABASE {db_name}''')
    cur.close()
    conn.close()
