saldo = 1000

while True:
    try:
        cantidad = int(input("Ingrese la cantidad a depositar: "))

        if cantidad < 0:
            print("Error: La cantidad debe ser un número entero positivo.")
        else:
            saldo += cantidad
            print("Depósito exitoso.")
            print("Su nuevo saldo es:", saldo)
            break

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
