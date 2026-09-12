##Declara una variable global llamada contador. Luego, crea una función que la modi
##fique y explique mediante un print() si fue necesario usar la palabra clave global.



contador = 0
def incrementar():
    global contador
    contador += 1
    print(f"Dentro de la función, contador = {contador}")

print(f"Antes de llamar: contador = {contador}")
incrementar()
incrementar()
incrementar()
print(f"Después de llamar: contador = {contador}")
