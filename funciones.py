from datetime import date
from random import randint

peliculas = []


def films():
    return peliculas


def add_film(texto):
    if texto not in peliculas:
        peliculas.append(texto)


def day_film():
    random = randint(0, peliculas.len)
    pelicula = peliculas[random]
    peliculas.pop(random)
    return pelicula
