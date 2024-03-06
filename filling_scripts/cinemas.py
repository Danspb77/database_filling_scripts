import sqlite3
import random
import string
from datetime import datetime, timedelta


conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')


cursor = conn.cursor()
cursor.execute('''DROP TABLE IF EXISTS cinemas''')

cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cinema_name TEXT,
                    city TEXT,
                    country TEXT,
                    films_id INTEGER)
                  ''')



cinema_names = ["AMC Empire 25",
    "Odeon Leicester Square",
    "Grauman's Chinese Theatre",
    "El Capitan Theatre",
    "Cinéma Pathé Tuschinski",
    "Cinecittà",
    "Kino International",
    "Palace of the Governors",
    "Cine Opera",
    "Toho Cinemas",
    "Cine Joia",
    "Roxy Theatre",
    "PVR Cinemas",
    "Cine de Chef",
    "The Paris Theatre",
    "Palais des Festivals et des Congrès",
    "The Grand Rex",
    "Cinéma du Panthéon",
    "Tuschinski Theater",
    "Cinéma de Luxe"]
countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Russia', 'China', 'Japan', 'Brazil']

cities = [
    "New York",
    "London",
    "Los Angeles",
    "Los Angeles",
    "Amsterdam",
    "Rome",
    "Berlin",
    "Santa Fe",
    "Buenos Aires",
    "Tokyo",
    "Rio de Janeiro",
    "Toronto",
    "Mumbai",
    "Seoul",
    "New York",
    "Cannes",
    "Paris",
    "Paris",
    "Amsterdam",
    "Paris"
]


for _ in range(len(cinema_names)):

    cinema_name = cinema_names[_]
    city = random.choice(cities)
    country = random.choice(countries)
    film_id= random.randint(1,20)

    cursor.execute("INSERT INTO cinemas (cinema_name,city,country,films_id) VALUES (?,?,?,?)", (cinema_name,city,country,film_id))






# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()
