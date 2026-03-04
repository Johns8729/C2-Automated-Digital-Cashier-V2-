historial = ""

print("Su saldo es:", saldo)
historial = historial + "Consultó saldo\n"

saldo = saldo - retiro
historial = historial + "Retiro de $" + str(retiro) + "\n"

saldo = saldo + deposito
historial = historial + "Depósito de $" + str(deposito) + "\n"

print("\nHistorial de operaciones:")

if historial == "":
    print("No se realizaron operaciones")
else:
    print("----------------------------------")
    print(f"=========={historial}==========")
    print("----------------------------------")
