class Persona:

    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera


    def __str__(self) :
        return f"{self.nombre} tiene {self.edad} años de edad es de la carrera de {self.carrera}"
        
    def hablidad(self):
        print(f"{self.nombre} es rapido")
              
Persona_1 = Persona("Cristopher", 19, "TICS")

print(Persona_1)
Persona_1.hablidad()   

