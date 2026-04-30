from enum import Enum
class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen,
                 diametro, distancia_sol, tipo, es_observable):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print("Nombre del planeta =", self.nombre)
        print("Cantidad de satélites =", self.cantidad_satelites)
        print("Masa del planeta =", self.masa)
        print("Volumen del planeta =", self.volumen)
        print("Diámetro del planeta =", self.diametro)
        print("Distancia al sol =", self.distancia_sol)
        print("Tipo de planeta =", self.tipo.value)
        print("Es observable =", self.es_observable)

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        limite = 149_597_870 * 3.4
        return self.distancia_sol > limite

p1 = Planeta(
    "Tierra", 1, 5.9736E24, 1.08321E12,
    12742, 150_000_000, TipoPlaneta.TERRESTRE, True
)

p1.imprimir()
print("Densidad del planeta =", p1.calcular_densidad())
print("Es planeta exterior =", p1.es_planeta_exterior())
print()

p2 = Planeta(
    "Júpiter", 79, 1.899E27, 1.4313E15,
    139820, 750_000_000, TipoPlaneta.GASEOSO, True
)

p2.imprimir()
print("Densidad del planeta =", p2.calcular_densidad())
print("Es planeta exterior =", p2.es_planeta_exterior())
