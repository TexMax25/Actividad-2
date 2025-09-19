"""
Esta clase define objetos que representan una cuenta bancaria.
"""
class CuentaBancaria:
    # Atributo de clase para el porcentaje de interés mensual.
    porcentaje_interes_mensual = 0.01

    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta}")
        print(f"Saldo = ${self.saldo:,.2f}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a retirar es inválido o excede el saldo actual.")
            return False

    def calcular_interes(self):
        interes_ganado = self.saldo * self.porcentaje_interes_mensual
        self.saldo += interes_ganado
        print(f"Interés aplicado del {self.porcentaje_interes_mensual * 100}%.")
        print(f"Interés ganado: ${interes_ganado:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")


# Bloque principal para probar la clase
if __name__ == "__main__":
    TIPO_AHORROS = "AHORROS"
    TIPO_CORRIENTE = "CORRIENTE"

    # Se crea una nueva cuenta con los datos de Juan Rodríguez
    cuenta = CuentaBancaria("Juan", "Rodríguez", 987654321, TIPO_CORRIENTE)

    print("--- Datos iniciales de la cuenta ---")
    cuenta.imprimir()
    print("-" * 35)

    print("--- Operaciones de consignación y retiro ---")
    cuenta.consignar(150000)
    cuenta.consignar(75000)
    cuenta.retirar(100000)
    print("-" * 35)

    print("--- Cálculo de interés ---")
    cuenta.calcular_interes()
    print("-" * 35)