##Escribe una función llamada imprimir_clave_valor(**kwargs) que reciba cual
##quier número de argumentos con nombre (clave=valor) e imprima cada clave con su
##valor en una línea.


def imprimir_clave_valor(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_clave_valor(nombre="Ana", edad=22, ciudad="Bogotá")
