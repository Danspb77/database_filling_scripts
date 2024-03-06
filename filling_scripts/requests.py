import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('/home/kali/Documents/education/HOD/hod.db')
cursor = conn.cursor()

# Создаем курсор для выполнения операций с базой данных
cursor = conn.cursor()



# cursor.execute('SELECT film_id FROM numbers_in_films WHERE budget_in_millions = MAX(budget_in_millions')







# название кинотеатра, в котором показывали фильм из Китая
cursor.execute('SELECT cinema_name FROM cinemas WHERE films_id = (SELECT id WHERE country = "China")')

# имя актёра, который снимался в фильме, выпущенном в  1959 
cursor.execute('SELECT name FROM actors WHERE films_id = (SELECT id FROM movies WHERE release_year = 1959)')

# вывести актёров из USA
cursor.execute('SELECT name FROM actors WHERE country = "USA"')

# вывод названия фильма, у которго режиссёр Ridley Scott
cursor.execute('SELECT title FROM movies   WHERE ID = \
               (SELECT director_id FROM DIRECTORS WHERE name = "Ridley Scott" )')

# вывод названия фильма с самым маленьким бюджетом
cursor.execute("SELECT title FROM movies WHERE id = \
    (SELECT film_id FROM numbers_in_films WHERE budget_in_millions = \
    (SELECT MIN(budget_in_millions) FROM numbers_in_films))")

results = cursor.fetchall()

# Выводим результат на экран
for raw in results:
    print(raw)

# Закрываем соединение
conn.close()