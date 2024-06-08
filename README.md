# Курсовая по БД — работа с данными с hh.ru
![Static Badge](https://img.shields.io/badge/python-brightgreen?style=flat-square&color=1E90FF)
![Static Badge](https://img.shields.io/badge/postgreSQL-brightgreen?style=flat-square&color=9BED00)
![Static Badge](https://img.shields.io/badge/pgadmin4-brightgreen?style=flat-square&color=FFE800)
[![Badge](https://bs9x3sczg2ts.runkit.sh)](https://git.io/gradientbadge)
[![Badge](https://g3htzrfjzet3.runkit.sh)](https://git.io/gradientbadge)
![Static Badge](https://img.shields.io/badge/build-vismanor-brightgreen?style=flat-square&logo=appveyor&logoColor=FF800F&logoSize=auto&label=made%20by&labelColor=33AE42&color=F649A4&cacheSeconds=3600&link=vismanor)

Приложение позволяет получать данные о компаниях и вакансиях с API HH, 
спроектировать таблицы в БД PostgreSQL и загрузить полученные данные 
в созданные таблицы.

Были трудности с оформлением результатов выборки, однако теперь пользователь сможет
получить приемлемо структурированный результат выборки в консоли без 
огромного количества вложенных данных.

### ER-диаграмма:
![Без имени](https://github.com/vismanor/coursework-5/assets/147613028/136389d8-32c5-4cb4-ad7b-f6cd18aecbf7)

## Используемые технологии
* python
* requests, psycopg2


## Инструкция по развертыванию:

1. Введите в терминале следующую команду

```
git clone git@github.com:vismanor/coursework-5
```
2. Создайте виртуальное окружение
```
python3 -m venv venv
```
3. Активируйте виртуальное окружение
```
source venv/Scripts/activate
```
4. Создайте файл 'database.ini'
5. Добавьте в него **_свои_** данные **_по шаблону ниже_**

###### Шаблон
```
[postgresql]
USER=postrges
PASSWORD=postgres
HOST=localhost
PORT=5432
```

## Автор проекта:
Екатерина Смирнова, 
https://github.com/vismanor/
