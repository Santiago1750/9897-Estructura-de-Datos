lista = []
print(type(lista))

lista = [1,2,3,5]
print(lista)

lista = ["Diego", True, 3.14, 5, 4j, ["a", "b"], 4]
print(lista)

lista.append("santiago")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = ["a", "e", "e", "i", "o", "u"]
print(lista2.count("e"))

print(len(lista2))

print(lista2[4])
print(lista2[5])

lista2.pop()
print(lista2)

lista2.remove("a")
lista2.remove("e")
lista2.remove("e")
print(lista2)

lista2.reverse()
print(lista2)

lista2.sort()
print(lista2)

lista2 = ["a", "b", "B", "c"]
lista2.sort()
print(lista2)

tupla = ("Quito", "Guayaquil", "Cuenca", "Quito")
print(type(tupla))

# tupla.append("Machala")
# print(tupla)
print(tupla.count("Quito"))
print(tupla.index("Cuenca"))
# print(tupla.index("Quito"))

lista = list(tupla)

print(lista)
print(tupla)

list.append("Machala")
tupla = tuple(lista)

print(lista)
print(tupla)

# Range

rango = range(5, 10, 2)
print(type(rango))
print(rango)