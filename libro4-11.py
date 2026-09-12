##Usa un ciclo for y la sentencia break para recorrer una lista de números. El ciclo
##debe detenerse al encontrar un número negativo, e imprimir un mensaje indicando
##que se encontró.
##

numeros = [5, 8, 12, 3, -7, 20, 4]
for numero in numeros:
    if numero < 0:
        print(f"Se encontro un numero negativo: {numero}")
        break
    print(f"Numero positivo: {numero}")

print("Fin?.")
