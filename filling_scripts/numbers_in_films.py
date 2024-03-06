import sqlite3
import random

# Создаем подключение к базе данных
conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

# Создаем курсор для выполнения операций с базой данных
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS numbers_in_films''')
# Создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS numbers_in_films
                    (film_id INTEGER PRIMARY KEY ,
                    rating integer,
                    budget_in_millions integer)''')
for i in range(20):
    rating=random.randint(30,95)/10
    budget=random.randint(30,150)
    cursor.execute("INSERT INTO numbers_in_films (rating,budget_in_millions) VALUES (?,?)", (rating,budget,))

cursor.execute("INSERT INTO numbers_in_films (rating,budget_in_millions) VALUES (?,?)", (3,budget,))
# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()
