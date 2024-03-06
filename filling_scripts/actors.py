import sqlite3
import random
import string
from datetime import datetime, timedelta


conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')


cursor = conn.cursor()
cursor.execute('''DROP TABLE actors''')

cursor.execute('''CREATE TABLE IF NOT EXISTS actors
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    birth INTEGER,
                    country TEXT,
                    films_id INTEGER)
                  ''')


actors = [
    "Tom Hanks", "Leonardo DiCaprio", "Meryl Streep", "Brad Pitt", "Jennifer Lawrence",
    "Johnny Depp", "Robert De Niro", "Emma Stone", "Denzel Washington", "Scarlett Johansson",
    "Marlon Brando",
    "Audrey Hepburn",
    "Sean Connery",
    "Clint Eastwood",
    "Al Pacino",
    "Robert De Niro",
    "Jack Nicholson",
    "Morgan Freeman",
    "Dustin Hoffman",
    "Anthony Hopkins",
    "Robert Redford",
    "Jane Fonda",
    "Julie Andrews",
    "Michael Caine",
    "Harrison Ford",
    "Gene Hackman",
    "Catherine Deneuve",
    "Sophia Loren",
    "Paul Newman"
    
]


names = random.choices(actors, k=100)


def generate_random_birthday():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2000, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

# Список стран для генерации
countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Russia', 'China', 'Japan', 'Brazil']

# Вставляем значения в таблицу "actors" 100 раз
for _ in range(len(actors)):
    name = actors[_]
    birthday = generate_random_birthday()
    country = random.choice(countries)
    film_id= random.randint(1,20)
    cursor.execute("INSERT INTO actors (name,birth,country,films_id) VALUES (?,?,?,?)", (name,birthday,country,film_id))

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()
