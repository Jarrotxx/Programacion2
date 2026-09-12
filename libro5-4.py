##Escribe una función saludo_personalizado(nombre, mensaje) que imprima un
##saludo con nombre y un mensaje opcional. Si no se proporciona mensaje, debe usar
##“¡Que tengas un buen día!” por defecto. Prueba la función con y sin el segundo
##argumento


def saludo_personalizado(nombre, mensaje="que tengas un buen dia!"):
    print(f"Hola, {nombre}. {mensaje}")
saludo_personalizado("Ana", "Bienvenida al curso")
saludo_personalizado("Luis")
