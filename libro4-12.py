##Desafío: Escribe un programa que simule un cajero automático. El usuario inicia con
##$500. En cada iteración puede retirar un monto ingresado por teclado. El ciclo ter
##mina si el usuario escribe 0 o si el saldo es insuficiente. Muestra el saldo actualizado



saldo = 500
print(f"saldo inicial: ${saldo}")
print("introduce el monto a retirar (0 para salir):")
while True:
    monto = float(input("> "))
    if monto == 0:
        print("has decidido salir.")
        break
    if monto < 0:
        print("el monto no puede ser negativo. Intentalo de nuevo.")
        continue
    if monto > saldo:
        print(f"saldo insuficiente. Solo tienes ${saldo:.2f}.")
        break
    saldo -= monto
    print(f"retiro de ${monto:.2f} realizado. Saldo actual: ${saldo:.2f}")
print(f"saldo final: ${saldo:.2f}")
print("gracias por usar el cajero")
