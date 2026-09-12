##Crea dos conjuntos: A = {1, 2, 3, 4} y B = {3, 4, 5, 6}. Luego, muestra por
##pantalla:
##La unión de ambos conjuntos.
##La intersección.
##La diferencia de A menos B

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A)
print(B)
union = A | B
interseccion = A & B
diferencia = A - B
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia A-B: {diferencia}")
