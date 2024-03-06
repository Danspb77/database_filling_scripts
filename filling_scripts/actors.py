import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

# Drop the 'actors' table if it exists
cursor.execute('''DROP TABLE IF EXISTS actors''')

# Create the 'actors' table
cursor.execute('''CREATE TABLE IF NOT EXISTS actors
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    birth DATE,
                    country TEXT,
                    film_id INTEGER)
                  ''')

# List of actors
actors = [
    "Tom Hanks", "Leonardo DiCaprio", "Meryl Streep", "Brad Pitt", "Jennifer Lawrence",
    "Johnny Depp", "Robert De Niro", "Emma Stone", "Denzel Washington", "Scarlett Johansson",
    "Marlon Brando", "Audrey Hepburn", "Sean Connery", "Clint Eastwood", "Al Pacino",
    "Robert De Niro", "Jack Nicholson", "Morgan Freeman", "Dustin Hoffman", "Anthony Hopkins",
    "Robert Redford", "Jane Fonda", "Julie Andrews", "Michael Caine", "Harrison Ford",
    "Gene Hackman", "Catherine Deneuve", "Sophia Loren", "Paul Newman"
]

# Generate random birthday
def generate_random_birthday():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2000, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

# List of countries
countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Russia', 'China', 'Japan', 'Brazil']

# Insert values into the 'actors' table
for actor in actors:
    name = actor
    birthday = generate_random_birthday()
    country = random.choice(countries)
    film_id = random.randint(1, 20)  # Assuming 20 films exist
    cursor.execute("INSERT INTO actors (name, birth, country, film_id) VALUES (?, ?, ?, ?)", (name, birthday, country, film_id))

# Commit changes to the database
conn.commit()

# Retrieve and print all records from the 'actors' table
cursor.execute("SELECT * FROM actors")
actors = cursor.fetchall()
for actor in actors:
    print(actor)

# Close the database connection
conn.close()
