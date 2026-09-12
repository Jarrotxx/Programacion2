##Crea un diccionario que contenga información sobre una película: título, director y
##año. Luego:
##Accede al valor de cada clave con print().
##Agrega una nueva clave llamada género.
##Modifica el año.


pelicula = {
    "titulo": "El Padrino",
    "director": "Francis Ford Coppola",
    "año": 1972
}
print(f"Título:   {pelicula['titulo']}")
print(f"Director: {pelicula['director']}")
print(f"Año:      {pelicula['año']}")
pelicula["género"] = "Drama"
pelicula["año"] = 1973
del pelicula["director"]
print("Diccionario final:")
print(pelicula)
