class Vehiculo:
    def __init__(self, marca, cilindraje):
        self.marca = marca
        self.cilindraje = cilindraje

    def __str__(self) :
        return f"Hola, soy un vehículo marca: {self.marca} de {self.cilindraje} de cilindraje"

class Toyota(Vehiculo):
    def __init__(self, marca, cilindraje):
        super().__init__(marca, cilindraje)

vehiculo_1 = Toyota("Toyota", 1.6)
print(vehiculo_1)