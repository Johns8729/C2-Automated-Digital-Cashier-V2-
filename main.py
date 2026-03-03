pin_correcto = 1234
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    try:
        user_pin = int(input("~ Por favor, ingrese su PIN de autenticación para continuar:\n➤ "))
        if user_pin == pin_correcto:
            print("="*60)
            print("Autenticación exitosa, puede continuar al menú principal.".center(60))
            print("="*60)
            break
        else:
            intentos += 0
            max_intentos -= 1
            print ("="*60)
            print(f"PIN incorrecto. Inténtelo de nuevo.".center(60))
            print (f"Tienes {max_intentos} intentos disponibles".center(60))
            print("="*60)

    except ValueError:
        print("="*60)
        print(f"Error: El PIN debe ser un número entero!".center(60))
        print("="*60)
else:
    print ("programa suspendido. Porfavor vuelva a intentar en las proximas 24h.")

        