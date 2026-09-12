##Dado un texto, cuenta cuántas veces aparece la letra “a” (minúscula) usando un
##ciclo for


texto = input("Ingrese el testo: ")
contador = 0
for letra in texto:
    if letra == "a":
        contador += 1
print(f"La letra 'a' aparece {contador} veces.")
