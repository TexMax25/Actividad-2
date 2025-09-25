
from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diesel"
    BIODIESEL = "Biodiesel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible: TipoCombustible,tipo_automovil: TipoAutomovil, numero_puertas, cantidad_asientos,velocidad_maxima, color: Color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

    def get_marca(self): return self.marca
    def get_modelo(self): return self.modelo
    def get_motor(self): return self.motor
    def get_tipo_combustible(self): return self.tipo_combustible
    def get_tipo_automovil(self): return self.tipo_automovil
    def get_numero_puertas(self): return self.numero_puertas
    def get_cantidad_asientos(self): return self.cantidad_asientos
    def get_velocidad_maxima(self): return self.velocidad_maxima
    def get_color(self): return self.color
    def get_velocidad_actual(self): return self.velocidad_actual

    def set_marca(self, valor): self.marca = valor
    def set_modelo(self, valor): self.modelo = valor
    def set_motor(self, valor): self.motor = valor
    def set_tipo_combustible(self, valor: TipoCombustible): self.tipo_combustible = valor
    def set_tipo_automovil(self, valor: TipoAutomovil): self.tipo_automovil = valor
    def set_numero_puertas(self, valor): self.numero_puertas = valor
    def set_cantidad_asientos(self, valor): self.cantidad_asientos = valor
    def set_velocidad_maxima(self, valor): self.velocidad_maxima = valor
    def set_color(self, valor: Color): self.color = valor
    def set_velocidad_actual(self, valor):
        if valor < 0:
            print("No se puede establecer velocidad negativa. Se pone 0 km/h.")
            self.velocidad_actual = 0
        elif valor > self.velocidad_maxima:
            print("No se puede superar la velocidad máxima. Se pone velocidad máxima.")
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual = valor

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")
        else:
            self.velocidad_actual += incremento
            print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento < 0:
            print("No se puede decrementar a una velocidad negativa.")
        else:
            self.velocidad_actual -= decremento
            print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self):
        self.velocidad_actual = 0
        print(f"El automóvil ha frenado. Velocidad actual: {self.velocidad_actual} km/h")

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual <= 0:
            print("No se puede calcular tiempo con velocidad cero.")
            return None
        return distancia / self.velocidad_actual

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor} L")
        print(f"Tipo de combustible = {self.tipo_combustible.value}")
        print(f"Tipo de automóvil = {self.tipo_automovil.value}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima} km/h")
        print(f"Color = {self.color.value}")
        print(f"Velocidad actual = {self.velocidad_actual} km/h")

if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO,5, 6, 250, Color.NEGRO)
    auto1.imprimir()
    auto1.set_velocidad_actual(100)
    auto1.acelerar(20)
    auto1.desacelerar(50)
    auto1.frenar()
