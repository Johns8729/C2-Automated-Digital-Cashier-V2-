def validar_entero_positivo(mensaje):
   
    while True:
        try:
            valor = int(input(mensaje))

            if valor <= 0:
                print("Error: Debe ingresar un número mayor que cero.")
                continue

            return valor

        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero.")


def validar_entero_no_negativo(mensaje):
   
    while True:
        try:
            valor = int(input(mensaje))

            if valor < 0:
                print("Error: No se permiten números negativos.")
                continue

            return valor

        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero.")


def validar_opcion_menu(mensaje, opciones_validas):
 
    while True:
        try:
            opcion = int(input(mensaje))

            if opcion not in opciones_validas:
                print("Error: Opción no válida.")
                continue

            return opcion

        except ValueError:
            print("Error: Debe ingresar un número válido.")


def validar_monto_retiro(mensaje, saldo):

    while True:
        try:
            monto = int(input(mensaje))

            if monto <= 0:
                print("Error: El monto debe ser mayor que cero.")
                continue

            if monto > saldo:
                print("Error: Saldo insuficiente. ")
                continue

            return monto

        except ValueError:
            print("Error: Entrada invalida. Ingrese un numero entero. ")