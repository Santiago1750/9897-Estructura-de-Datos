
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

tupla = ("Quito", "Guayaquil", "Cuenca", "Quito")
tupla2 = set(tupla)
print(tupla2)
print (type(tupla))

print(tupla.count("Quito"))
print(tupla.index("Cuenca"))
# print(tupla.index("Quito"))

lista = list(tupla)
print(lista)
print(tupla)

lista.append("Machala")
tupla = tuple(lista)

print(tupla)
print(lista)


# RANGE

rango = range(5, 10)
print(type(rango))
print(rango)


# Sets

conjunto = {"i", "o", "a", "e", "u", "a", "a", "a" }
print(type(conjunto))
print(conjunto)

#diccionario

cliente001 = {"nombre": "Cristopher", 
              "apellido": "Lasluisa",
              "telefono": "0963356124",
              "correo": "cristo@gmail.com" 
            }

print(type(cliente001))
print(cliente001["nombre"])
print(cliente001["correo"])

print(cliente001.get("telefono"))
cliente001["nombre"]="Juan"
print(cliente001)
print(len(cliente001))

cliente001.popitem()
print(cliente001)

cliente001.pop("apellido")
print(cliente001)

del cliente001["telefono"]
print(cliente001)

#Bolean

mayorEdad=True
open = False