## Dado el texto "Hola Mundo.", completa las siguientes instrucciones utilizando los
##métodos de cadena adecuados para lograr el resultado deseado:
##a) Convertir la frase a mayusculas.
##b) Convertir la frase a minusculas.
##c) Reemplazar la palabra (Mundo) por la palabra (Universo).

texto = "Hola Mundo."
mayusculas = texto.upper()
minusculas = texto.lower()
reemplazado = texto.replace("Mundo", "Universo")
print(f"Mayusculas: {mayusculas}")
print(f"Minusculas: {minusculas}")
print(f"Reemplazo: {reemplazado}")
