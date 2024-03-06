import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

# Drop the 'directors' table if it exists
cursor.execute('''DROP TABLE IF EXISTS directors''')

# Create the 'directors' table
cursor.execute('''CREATE TABLE IF NOT EXISTS directors
                  (director_id INTEGER PRIMARY KEY,
                  name TEXT,
                  country TEXT,
                  age INTEGER)
               ''')

# List of countries
countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Russia', 'China', 'Japan', 'Brazil']

directors = [
    "Steven Spielberg", "Martin Scorsese", "Christopher Nolan", "Quentin Tarantino", "Alfred Hitchcock",
    "Stanley Kubrick", "Francis Ford Coppola", "James Cameron", "Ridley Scott", "Woody Allen",
    "Pedro Almodóvar", "Ang Lee", "Guillermo del Toro", "Wes Anderson", "Coen Brothers",
    "David Fincher", "Tim Burton", "Sofia Coppola", "Denis Villeneuve", "Akira Kurosawa"
]


for _ in range(10):
    name = directors[_]
    age = random.randint(20,70)
    country = random.choice(countries)
    cursor.execute("INSERT INTO directors (name,age,country) VALUES (?,?,?)", (name,age,country,))

conn.commit()

cursor.execute("select * from directors")
directors= cursor.fetchall()

for director in directors:
    print(director)

conn.close()
