import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base + self.base + self.altura + self.altura


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def hipotenusa(self):
        h = math.sqrt((self.base * self.base) + (self.altura * self.altura))
        return h

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def tipo_triangulo(self):
        h = self.hipotenusa()

        if self.base == self.altura and self.altura == h:
            print("El triangulo es equilatero")
        elif self.base == self.altura or self.base == h or self.altura == h:
            print("El triangulo es isosceles")
        else:
            print("El triangulo es escaleno")


# aqui se crean los objetos
circulo1 = Circulo(2)
rectangulo1 = Rectangulo(1, 2)
cuadrado1 = Cuadrado(3)
triangulo1 = Triangulo(3, 5)

print("Area del circulo:", circulo1.area())
print("Perimetro del circulo:", circulo1.perimetro())

print("Area del rectangulo:", rectangulo1.area())
print("Perimetro del rectangulo:", rectangulo1.perimetro())

print("Area del cuadrado:", cuadrado1.area())
print("Perimetro del cuadrado:", cuadrado1.perimetro())

print("Area del triangulo:", triangulo1.area())
print("Perimetro del triangulo:", triangulo1.perimetro())
print("Hipotenusa del triangulo:", triangulo1.hipotenusa())
triangulo1.tipo_triangulo()
