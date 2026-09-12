##Escribe un programa que use un ciclo while para pedir al usuario una contraseña.
##El programa debe seguir pidiendo hasta que el usuario escriba la contraseña correcta
##(por ejemplo, “python123”).


contrasena_correcta = "kierokeke"
contrasena = input("Introduce la contraseña: ")
while contrasena != contrasena_correcta:
    print("Contraseña incorrecta. Intentalo de nuevo.")
    contrasena = input("Introduce la contraseña: ")

print("Contraseña correcta Acceso concedido.")
