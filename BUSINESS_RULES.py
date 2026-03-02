# CONDICIONES DE RETIRO

except ValueError:
            print("\nMonto no válido. Por favor, ingrese un número entero.\n")
            continue
        while monto_retirar < 0:
            print("\nMonto no válido. Por favor, ingrese un monto positivo.\n")
            try:
                monto_retirar = int(input("ingrese el monto a retirar: "))
            except ValueError:
                print("\nMonto no válido. Por favor, ingrese un número entero.\n")
                continue
        if monto_retirar > saldo:
            print("\nFondos insuficientes\n")
        else:

#CONDICIONES DE DEPOSITO

try:       
    while deposito < 0:
        deposito=int(input("Error, ingrese un valor positivo: "))
        except ValueError:
            print("\nMonto no válido. Por favor, ingrese un número entero.\n")
            deposito = int(input("Ingrese el monto a depositar: ")) 