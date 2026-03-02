elif Opcion == 2:
        try:
            monto_retirar = int(input("\ningrese el monto a retirar: "))
        except ValueError:
            print("\nMonto no válido. Por favor, ingrese un número entero.\n")
            continue
        while monto_retirar < 0:
            print("\nMonto no válido. Por favor, ingrese un monto positivo.\n")
            try:
                monto_retirar = int(input("ingrese el monto a retirar: "))
           