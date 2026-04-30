from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diesel"
    BIODIESEL = "Biodiesel"
    GAS_NATURAL = "Gas Natural"

class TipoAuto(Enum):
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
    def __init__(self, marca, modelo, motor, tipo_combustible,
                 tipo_auto, puertas, asientos, velocidad_max, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_auto = tipo_auto
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self.color = color
        self.velocidad_actual = 0

    def get_velocidad_actual(self):
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad):
        self.velocidad_actual = velocidad

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_max:
            self.velocidad_actual += incremento
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad_actual

    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Tipo de combustible =", self.tipo_combustible.name)
        print("Tipo de automóvil =", self.tipo_auto.name)
        print("Número de puertas =", self.puertas)
        print("Cantidad de asientos =", self.asientos)
        print("Velocidad máxima =", self.velocidad_max)
        print("Color =", self.color.name)



auto = Automovil(
    "Ford", 2018, 3,
    TipoCombustible.DIESEL,
    TipoAuto.EJECUTIVO,
    5, 6, 250,
    Color.NEGRO
)

auto.imprimir()

auto.set_velocidad_actual(100)
print("Velocidad actual =", auto.get_velocidad_actual())

auto.acelerar(20)
print("Velocidad actual =", auto.get_velocidad_actual())

auto.desacelerar(50)
print("Velocidad actual =", auto.get_velocidad_actual())

auto.frenar()
print("Velocidad actual =", auto.get_velocidad_actual())

auto.desacelerar(20)