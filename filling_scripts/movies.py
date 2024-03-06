import sqlite3
import random

conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

cursor.execute('''DROP TABLE movies''')

cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                    (id INTEGER PRIMARY KEY ,
                    title TEXT,
                    genre TEXT,
                    release_year INTEGER,
                    director_id INTEGER)

                  
                  ''')



director_id=random.randint(1,7)
release_year= random.randint(1950,2020)

genres=['Drama','Crime''Sci-Fi','Comedy','Fantasy']
genre=genres[random.randint(0,len(genres)-1)]

titles = [
    "Tenet",
    "Mulan",
    "Soul",
    "The Invisible Man",
    "Birds of Prey",
    "The Gentlemen",
    "1917",
    "Parasite",
    "Onward",
    "Joker",
    "Hamilton",
    "Bad Boys for Life",
    "The Trial of the Chicago 7",
    "Da 5 Bloods",
    "The Old Guard",
    "Enola Holmes",
    "Extraction",
    "Palm Springs",
    "The Midnight Sky",
    "The King of Staten Island"
]

for _ in range(len(titles)):
    genre=genres[random.randint(0,len(genres)-1)]
    director_id=random.randint(1,7)
    release_year= random.randint(1950,2020)
    title=titles[random.randint(0,len(titles)-1)]
    cursor.execute("INSERT INTO movies (title,genre,release_year,director_id) VALUES (?,?,?,?)", (title,genre,release_year,director_id,))






# Сохраняем изменения
conn.commit()


cursor = conn.cursor()


cursor.execute("SELECT * FROM movies")


films = cursor.fetchall()

# Выводим результат на экран
for film in films:
    print(film)


conn.close()
