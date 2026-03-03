"""Feature: Athentication Process
Made by: Oscar Corzo
Date: 2024-06-01"""

saldo = 1000
pin = 1234

while True:
    try:
        user_pin = int(input("Por favor, ingrese su PIN de autenticación para continuar: "))
        if user_pin == pin:
            print("Autenticación exitosa, puede continuar al menú principal.")
            break
        else:
            print("\nPIN incorrecto. Inténtelo de nuevo.\n")

#Espacio para la Feature: attemtps control draft

    except ValueError:
        print("\nError: El PIN debe ser un número entero!\n")
        
