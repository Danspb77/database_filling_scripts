import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

# Drop the 'numbers_in_films' table if it exists
cursor.execute('''DROP TABLE IF EXISTS numbers_in_films''')

# Create the 'numbers_in_films' table
cursor.execute('''CREATE TABLE IF NOT EXISTS numbers_in_films
                    (film_id INTEGER PRIMARY KEY,
                    rating REAL,
                    budget_in_millions INTEGER)
                  ''')

# Generate and insert random data into the 'numbers_in_films' table
for _ in range(20):
    rating = round(random.uniform(3.0, 9.5), 1)  # Generate a random floating-point number for rating
    budget = random.randint(30, 150)  # Generate a random integer for budget
    cursor.execute("INSERT INTO numbers_in_films (rating, budget_in_millions) VALUES (?, ?)", (rating, budget))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
