import sqlite3
import random

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

cinema_names = [
    "AMC Empire 25", "Odeon Leicester Square", "Grauman's Chinese Theatre",
    "El Capitan Theatre", "Cinéma Pathé Tuschinski", "Cinecittà", "Kino International",
    "Palace of the Governors", "Cine Opera", "Toho Cinemas", "Cine Joia", "Roxy Theatre",
    "PVR Cinemas", "Cine de Chef", "The Paris Theatre", "Palais des Festivals et des Congrès",
    "The Grand Rex", "Cinéma du Panthéon", "Tuschinski Theater", "Cinéma de Luxe"
]

countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Russia', 'China', 'Japan', 'Brazil']

cities = [
    "New York", "London", "Los Angeles", "Amsterdam", "Rome",
    "Berlin", "Santa Fe", "Buenos Aires", "Tokyo", "Rio de Janeiro",
    "Toronto", "Mumbai", "Seoul", "Cannes", "Paris"
]

# Insert values into the 'cinemas' table
for cinema_name in cinema_names:
    city = random.choice(cities)
    country = random.choice(countries)
    film_id = random.randint(1, 20)  # Assuming 20 films exist
    cursor.execute("INSERT INTO cinemas (cinema_name, city, country, films_id) VALUES (?, ?, ?, ?)",
                   (cinema_name, city, country, film_id))

# Commit changes to the database
conn.commit()

# Retrieve and print all records from the 'cinemas' table
cursor.execute("SELECT * FROM cinemas")
cinemas = cursor.fetchall()
for cinema in cinemas:
    print(cinema)

# Close the database connection
conn.close()
