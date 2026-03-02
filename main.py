saldo = 1000

while True:
    try:
        cantidad = int(input("Ingrese la cantidad a depositar: "))
#Acá va el condicional if para que busca arreglar el error cuando se ingresa un número negativo o racional
            saldo += cantidad
            print("Depósito exitoso.")
            print("Su nuevo saldo es:", saldo)
            break

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
