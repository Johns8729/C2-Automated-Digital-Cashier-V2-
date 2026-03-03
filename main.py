saldo = 100
limite_diario_retiro=800 
retiro_diario=0
elif Opcion == 2:
    monto_retirar = int(input("\ningrese el monto a retirar: "))

    if retiro_diario+monto_retirar > limite_diario_retiro:
     print("Usted ha excedido el límite diario de retiro.")
    
    else:
        print("limite diario disponible hoy: ", limite_diario_retiro)
        saldo -= monto_retirar
        retiro_diario += monto_retirar
        print(F"\nRetiro exitoso. Su nuevo saldo actualizado es de: {saldo}\n")
        print("\nGracias por usar el cajero automático")
