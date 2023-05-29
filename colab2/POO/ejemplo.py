
class Monster:

    def __init__(self,  nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def myFunc(self):
        print("Hey, yo soy un " ,self.categoria)   

monstruito = Monster("Sullivan", "Asustador") 

print(monstruito.nombre)
print(monstruito.myFunc)