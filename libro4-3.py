## Solicita al usuario dos números y un operador (+,-, *, /). Usa una estructura
##condicional para realizar la operación correspondiente. Si el operador no es válido,
##muestra un mensaje de error.
##

num1 = float(input("introduce el primer numero: "))
num2 = float(input("introuce el segundo numero: "))
operador = input("introduce el operador (+, -, *, /): ")
if operador == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 == 0:
        print("error: no se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
else:
    print(f"error: el operador '{operador}' no es valido.")
