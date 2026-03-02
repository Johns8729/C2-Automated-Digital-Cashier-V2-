opcion = 3 
if opcion == 3:
    deposito = int(input("digite la cantidad a depositar: "))
while deposito < 0:
    deposito = int(input("Error, ingrese un valor positivo: "))
    

    if opcion == 3:
        
        try: 
            deposito = int(input("Ingrese el monto a depositar: "))
            while deposito < 0:
                deposito=int(input("Error, ingrese un valor positivo: "))
        except ValueError:
            print("\nMonto no válido. Por favor, ingrese un número entero.\n")
            deposito = int(input("Ingrese el monto a depositar: ")) 

        if deposito > 0:
            print ("Su nuevo saldo es: ", saldo+deposito)


print(" Gracias por usar el cajero automatico")