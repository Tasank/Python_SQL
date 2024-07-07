# Импортировать пакет psycopg2
import psycopg2

# Открыть подключение к базе.
# Если вы меняли настройки своей БД, то и здесь им придётся
# указать соответствующие.
# Таких подключений можно открывать сколько угодно,
# если у вашего приложения данные распределены по нескольким базам
conn = psycopg2.connect("dbname=Школа user=postgres password=1234")

# Создать «курсор» на подключении к базе.
# Курсоры используются для представления
# сессий подключения к БД.
cur = conn.cursor()

# Удалить существующую таблицу, если она есть
cur.execute("DROP TABLE IF EXISTS tost;")

# Создать таблицу с правильной структурой
cur.execute(
    "CREATE TABLE tost (id serial PRIMARY KEY, num integer, data varchar);"
)

# Вставить данные
cur.execute(
    "INSERT INTO tost (num, data) VALUES (%s, %s)",
    (100, "abc'def")
)

# Выполнить команду
cur.execute("SELECT * FROM test;")
# Получить результат её выполнения
print(cur.fetchone())

# Завершить транзакцию
conn.commit()
# Закрыть курсор
cur.close()
# Закрыть подключение
conn.close()