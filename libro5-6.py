## Crea una función llamada sumar_todo(*args) que acepte cualquier cantidad de
##argumentos numéricos y retorne la suma total. Prueba la función con 3, 5 y hasta
##7 números.



def sumar_todo(*args):
    return sum(args)
print(sumar_todo(1, 2, 3))
print(sumar_todo(10, 20, 30, 40, 50))
print(sumar_todo(1, 2, 3, 4, 5, 6, 7))
