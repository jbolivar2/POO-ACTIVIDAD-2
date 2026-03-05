class Operaciones:

    def mensaje(self):
        print("Vamos a sumar dos numeros")

    def sumar(self, x, y):
        return x + y


op = Operaciones()

op.mensaje()

num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))

resultado = op.sumar(num1, num2)

print("Resultado:", resultado)
