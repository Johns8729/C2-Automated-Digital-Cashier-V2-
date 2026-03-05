    if Opcion == 2:
        while True:    
            try:
                monto_retirar = int(input("\ningrese el monto a retirar: "))

                saldo -= monto_retirar
                print(F"\nRetiro exitoso. Su nuevo saldo actualizado es de: {saldo}\n")
                