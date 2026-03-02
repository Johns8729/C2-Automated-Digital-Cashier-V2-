elif Opcion == 2:
        try:
            monto_retirar = int(input("\ningrese el monto a retirar: "))
            
        #aqui van los condicionales

            saldo -= monto_retirar
            print(F"\nRetiro exitoso. Su nuevo saldo actualizado es de: {saldo}\n")
            print("\nGracias por usar el cajero automático")