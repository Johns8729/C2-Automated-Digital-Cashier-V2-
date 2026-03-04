# CONFIGURACION INICIAL, VAMOS A DETERMINAR LAS VARIABLES 
print("BIENVENIDO AL CAJERO ATM TECH BANK RIWI DIGITAL")
saldo =  1000
pint_correcto = 1234
intentos_maximos = 3 
sesion_activa = False
intentos = 0 
cuenta_1 = 1234

cuenta_1 = input("Ingrese su Nombr de Usuario: ")

# Lo siguiente le tocaria a la persona de autenticacion

"""Feature: Athentication Process
Made by: Oscar Corzo
Date: 2024-06-01"""

while True:
    try:
        user_pin = int(input("~ Por favor, ingrese su PIN de autenticación para continuar:\n➤ "))
        if user_pin == pin:
            print("="*60)
            print("Autenticación exitosa, puede continuar al menú principal.".center(60))
            print("="*60)
            break
        else:
            print("="*60)
            print(f"PIN incorrecto. Inténtelo de nuevo.".center(60))
            print("="*60)
            
# Espacio para la Feature: attemtps control

    except ValueError:
        print("="*60)
        print(f"Error: El PIN debe ser un número entero!".center(60))
        print("="*60)
