# CONDICIONES VALIDACION DE RETIRO

while monto_retirar <= 0:
    monto_retirar = int(input("El monto a retirar debe ser mayor que cero.Ingrese un nuevo monto: "))

    if monto_retirar > saldo:   
        print("✗ Fondos insuficientes.saldo actual: ", saldo)
            continue
