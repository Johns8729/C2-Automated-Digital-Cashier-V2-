saldo = 100
limite_diario_retiro=2000
retiro_diario=0
monto=0
try:
    monto =float(monto)
    if retiro_diario + monto > limite_diario_retiro:
        disponible = limite_diario_retiro-retiro_diario
        print(f"limite diario excedido. disponible hoy: ",disponible)
        

    saldo -= monto
    retiro_diario += monto
    print(f"✓ Retiro exitoso: ${monto:.2f}")
    print(f"Saldo actual: ${saldo:.2f}")
    

except ValueError:
    print("✗ Monto inválido")
