import sqlite3

# Connect to the SQLite database and create cursor
with sqlite3.connect('/home/kali/Documents/education/HOD/hod.db') as conn:
    cursor = conn.cursor()

    # Get the cinema name where films from China were shown
    cursor.execute('''SELECT cinema_name FROM cinemas 
                      WHERE films_id IN 
                          (SELECT id FROM movies WHERE country = "China")''')
    china_cinema = cursor.fetchone()
    print("Cinema showing films from China:", china_cinema[0] if china_cinema else "No such cinema found")

    # Get the actor names who starred in a film released in 1959
    cursor.execute('''SELECT name FROM actors 
                      WHERE film_id IN 
                          (SELECT id FROM movies WHERE release_year = 1959)''')
    actors_1959 = cursor.fetchall()
    print("Actors in films released in 1959:", [actor[0] for actor in actors_1959])

    # Get the actor names from USA
    cursor.execute('''SELECT name FROM actors WHERE country = "USA"''')
    usa_actors = cursor.fetchall()
    print("Actors from USA:", [actor[0] for actor in usa_actors])

    # Get the title of the film directed by Ridley Scott
    cursor.execute('''SELECT title FROM movies 
                      WHERE director_id IN 
                          (SELECT director_id FROM directors WHERE name = "Ridley Scott")''')
    ridley_scott_movie = cursor.fetchone()
    print("Film directed by Ridley Scott:", ridley_scott_movie[0] if ridley_scott_movie else "No such film found")

    # Get the title of the film with the smallest budget
    cursor.execute('''SELECT title FROM movies 
                      WHERE id IN 
                          (SELECT film_id FROM numbers_in_films 
                           WHERE budget_in_millions = (SELECT MIN(budget_in_millions) FROM numbers_in_films))''')
    lowest_budget_movie = cursor.fetchone()
    print("Film with the smallest budget:", lowest_budget_movie[0] if lowest_budget_movie else "No such film found")
