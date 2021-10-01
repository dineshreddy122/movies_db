import sqlite3
from movies import movies

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE movies (
            movie text,
            Lead Actor text,
            year of release integer,
            director
            )""")


def insert_movies(movies):
    with conn:
        c.execute("INSERT INTO movies VALUES (:movie, :Lead Actor, :actress,:year of release,:director)", {'movie': movies.movie, 'Lead Actor': movies.Lead Actor, 'actress': movies.actress,'year of release':movies.year of release,'director':movies.director})


def get_movies_by_movie(movie):
    c.execute("SELECT * FROM movies WHERE movie=:movie", {'movie': movie})
    return c.fetchall()


def update_director(movies,director):
    with conn:
        c.execute("""UPDATE movies SET director = :director
                    WHERE Lead Actor = :Lead Actor AND actress = :actress""",
                  {'Lead Actor': movies.LEad Actor, 'actress': movies.actress, 'director': director})


def remove_movie(movies):
    with conn:
        c.execute("DELETE from movies WHERE Lead Actor = :Lead Actor AND actress = :actress",
                  {'Lead Actor': movies.Lead Actor, 'actress': movies.actress})

movie_1 = movies('love story', 'Naga Chaitanya','Sai Pallavi','2021,'sheaker kamala')
movie_2 = movies('don't breathe', 'robein hood','alexander catreen','2019', 'steve hackingson')

insert_movie(movie_1)
insert_movie(movie_2)

movies = get_movie_by_name('love story')
print(movies)

update_director(movies_2, 'Raja mouli')
remove_movie(movie_2)

movies = get_movies_by_name('don't breathe')
print(movies)

conn.close()