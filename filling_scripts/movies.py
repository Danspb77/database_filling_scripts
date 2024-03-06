import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

# Create the 'movies' table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                    (id INTEGER PRIMARY KEY,
                    title TEXT,
                    genre TEXT,
                    release_year INTEGER,
                    director_id INTEGER)
                ''')

# Sample data
titles = [
    "Tenet", "Mulan", "Soul", "The Invisible Man", "Birds of Prey",
    "The Gentlemen", "1917", "Parasite", "Onward", "Joker",
    "Hamilton", "Bad Boys for Life", "The Trial of the Chicago 7",
    "Da 5 Bloods", "The Old Guard", "Enola Holmes", "Extraction",
    "Palm Springs", "The Midnight Sky", "The King of Staten Island"
]
genres = ['Drama', 'Crime', 'Sci-Fi', 'Comedy', 'Fantasy']

# Insert sample data into the 'movies' table
for _ in range(len(titles)):
    title = random.choice(titles)
    genre = random.choice(genres)
    release_year = random.randint(1950, 2020)
    director_id = random.randint(1, 7)
    cursor.execute("INSERT INTO movies (title, genre, release_year, director_id) VALUES (?, ?, ?, ?)", (title, genre, release_year, director_id))

# Commit the changes to the database
conn.commit()

# Retrieve and print all records from the 'movies' table
cursor.execute("SELECT * FROM movies")
films = cursor.fetchall()
for film in films:
    print(film)

# Close the database connection
conn.close()
