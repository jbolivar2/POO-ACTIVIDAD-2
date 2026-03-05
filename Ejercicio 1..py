class Persona:

    def __init__(self, nombre, apellido, documento, anio):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio = anio

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento:", self.documento)
        print("Año:", self.anio)
        print("")


print("Persona 1")
n1 = input("Nombre: ")
a1 = input("Apellido: ")
d1 = input("Documento: ")
an1 = input("Año nacimiento: ")

persona1 = Persona(n1, a1, d1, an1)

print("\nPersona 2")
n2 = input("Nombre: ")
a2 = input("Apellido: ")
d2 = input("Documento: ")
an2 = input("Año nacimiento: ")

persona2 = Persona(n2, a2, d2, an2)

print("\nDatos guardados:")
persona1.mostrar()
persona2.mostrar()
