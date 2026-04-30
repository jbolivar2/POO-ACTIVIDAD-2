class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0

    def imprimir(self):
        print("Nombres del titular:", self.nombres)
        print("Apellidos del titular:", self.apellidos)
        print("Numero de cuenta:", self.numero_cuenta)
        print("Tipo de cuenta:", self.tipo_cuenta)
        print("Saldo:", self.saldo)

    def consultar_saldo(self):
        print("El saldo actual es:", self.saldo)

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Se ha consignado:", valor)
            print("Nuevo saldo:", self.saldo)
        else:
            print("El valor a consignar debe ser mayor que cero")

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("Se ha retirado:", valor)
            print("Nuevo saldo:", self.saldo)
        else:
            print("No se puede retirar ese valor")
            print("El valor debe ser mayor que cero y no debe superar el saldo")


cuenta1 = CuentaBancaria("Pedro", "Perez", 123456789, "Ahorros")

cuenta1.imprimir()

print()

valor_consignar = int(input("Ingrese el valor que desea consignar: "))
cuenta1.consignar(valor_consignar)

valor_retirar = int(input("Ingrese el valor que desea retirar: "))
cuenta1.retirar(valor_retirar)

print()

cuenta1.consultar_saldo()
