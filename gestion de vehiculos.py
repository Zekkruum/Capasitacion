
#superclase llamada vehiculo para que se puedan crear distintos tipos de vehículos con un metodo heredado

class vehiculo:
    def __init__(self, marca, modelo, año, km):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.km= km

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.km}"

# herencia para distintos tipos de vehículos

class auto(vehiculo):
    def __init__ (self, marca, modelo, año, km, motor):
        super().__init__(marca, modelo, año, km)
        self.motor = motor
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Tipo de auto: {self.motor}"
    
class moto(vehiculo):
    def __init__ (self, marca, modelo, año, km, cilindrada):
        super().__init__(marca, modelo, año, km)
        self.cilindrada = cilindrada
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Cilindrada: {self.cilindrada}cc"

datos_auto = auto("Citröen", "Xsara" , 2000, 150000, "Sedán")
datos_moto = moto("Yamaha", "FZ", 2015, 30000, 150)

print(datos_auto.mostrar_info())
print(datos_moto.mostrar_info())

