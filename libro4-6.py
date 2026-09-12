## Crea un ciclo while que sume números ingresados por el usuario. El programa debe
##terminar cuando el usuario escriba “salir”. Al final, muestra la suma total.


suma = 0
entrada = input("Introduce un numero (o 'salir' para terminar): ")
while entrada.lower() != "salir":
    try:
        numero = float(entrada)
        suma += numero
    except ValueError:
        print("Eso no es un numero valido. Intentalo de nuevo.")
    entrada = input("Introduce un numero (o 'salir' para terminar): ")
print(f"La suma total es: {suma}")
