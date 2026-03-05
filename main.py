#breyner funcion depositar
 elif Opcion == 3:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad a depositar: "))
                def VALIDACION_DEPOSITO(monto):
                    if monto <= 0:
                        return False, "No se permiten montos negativos o cero"
                    return True, "Depòsito Valido!."
                saldo = saldo + cantidad
                historial = historial + "💰 Depósito de $" + str(cantidad) + "\n"
                print(f"\nSu nuevo saldo es de: ${saldo}")
                print("\nGracias por usar el cajero automático")
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
