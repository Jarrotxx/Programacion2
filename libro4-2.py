##Escribe un programa que solicite la edad del usuario y muestre un mensaje perso
##nalizado según su rango:
##Menor de 12: “Eres un niño”.
##Entre 12 y 17: “Eres un adolescente”.
##Entre 18 y 59: “Eres un adulto”.
##60 o más: “Eres un adulto mayor”

edad = int(input("Introduce tu edad: "))
if edad < 12:
    print("Eres un niño.")
elif edad <= 17:
    print("Eres un adolescente.")
elif edad <= 59:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
