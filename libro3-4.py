## ¿Qué sucede si intentas modificar un elemento de una tupla? Escribe un pequeño
##ejemplo y comenta el resultado.

datos = ("Jose", 19, "La Ceja")
print(datos)
print('19 se volvera 20, pero al ser tupla, no se va a poder ediar')
datos[1] = 20
print(datos)
