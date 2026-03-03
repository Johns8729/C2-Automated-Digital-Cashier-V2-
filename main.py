"""Feature: Athentication Process
Made by: Oscar Corzo
Date: 2024-06-01"""

saldo = 1000
pin = 1234

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
