##Escribe un programa que pida al usuario un número entero y muestre si es positivo,
##negativo o cero usando if, elif y else.


numero = int(input("Introduce un número entero: "))
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")
