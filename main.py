#breyner funcion depositar
 elif Opcion == 3:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a depositar: "))
                saldo = saldo + cantidad
                historial = historial + "💰 Depósito de $" + str(cantidad) + "\n"
                print(f"\nSu nuevo saldo es de: ${saldo}")
                print("\nGracias por usar el cajero automático")
                break
            except ValueError:
                print("Error: Ingrese un número entero válido.")
