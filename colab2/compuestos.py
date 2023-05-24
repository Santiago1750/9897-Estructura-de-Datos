
lista=[]
print(type(lista))

lista = [1, 2, 3, 4]

print(lista)

lista=["Cris", True, 3.14, 4j, ["a", "b"], 4]

print(lista)

lista.append("Juan")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 =["a", "e", "i", "i", "o", "u"]
print(lista2.count("i"))

print(len(lista2))

print(lista2[4])
print(lista2[5])

lista2.pop()
print(lista2)

lista2.remove("i")
lista2.remove("i")
lista2.remove("a")
print(lista2)

lista2.reverse()
print(lista2)

lista2.sort()
print(lista2)

lista2 = ["a", "b", "B", "c"]
lista2.sort()
print(lista2)