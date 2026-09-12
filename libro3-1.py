##Crea una lista con los nombres de tres frutas. Luego, agrega una fruta al final,
##elimina la primera y muestra la lista resultante con print().

frutas = ["manzana", "banana", "naranja"]
print(frutas)
print('Se adicionara "uva" al final de la lista y se borrara a "manzana"')
frutas.append("uva")
frutas.pop(0)
print(frutas)
