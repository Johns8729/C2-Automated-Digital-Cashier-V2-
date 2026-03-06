#(Jafet) FUNCION MENU
from time import sleep
import datetime
import time
welcome = """
╔════════════════════════════════════════════════════════════╗
                🏦 TECH BANK RIWI DIGITAL 🏦
            🙌¡Bienvenido al Cajero Automático!🙌
╚════════════════════════════════════════════════════════════╝
    """
# CONFIGURACION INICIAL, VAMOS A DETERMINAR LAS VARIABLES
welcome = """
╔════════════════════════════════════════════════════════════╗
    🏦 BIENVENIDO AL CAJERO ATM TECH BANK RIWI DIGITAL 🏦 
╚════════════════════════════════════════════════════════════╝
"""
for _ in welcome:
    print(_,end="",flush=True)
    sleep(0.005)

saldo =  1000
pint_correcto = 1234
intentos_maximos = 3 
sesion_activa = False
intentos = 0 
cuenta_1 = 1234
limite_diario_retiro=800 
retiro_diario=0
monto = 0
historial = ""
cuenta_1 = input("🤵Ingrese su Nombre de Usuario: ")

# """Feature: Athentication Process
# Made by: Oscar Corzo
# Date: 2026-03-05"""

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
            
            max_intentos -= 1  # bug corregido BY: JOSEPH ROMERO - el codigo original tenia "intentos += 0" lo cual nunca sumaba al contador generando un bucle infinito. Se elimino la linea redundante
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
    exit ()

Cant_Operaciones = 0
while Cant_Operaciones <= 0:
    try:
        Cant_Operaciones= int(input (f"\n{'Cuantas operaciones desea realizar?':^65}\n"))

        if Cant_Operaciones <=0:
             print(f"\n{'❌ Error: Ingrese un valor positivo ❌':^65}\n")

    except ValueError:
         print("Error: Ingrese un número entero válido.")
         
         

for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion= 0
    while Opcion <= 0:
        try:              
            Opcion = int(input(f"""--------------- Menú Principal --------------- | #{Conteo} 
        1) 🔍 Consultar saldo 
        2) 💳 Retirar dinero 
        3) 💰 Depositar dinero 
        4) ✅ Finalizar
        ==================================================
        Seleccione una opción:
        ➤ """)) 
            if Opcion <=0:
                print(f"\n{'❌ Error: Ingrese un valor positivo ❌':^65}\n")  

            if Opcion < 1 or Opcion > 4:
                print("\nERROR: Por favor ingrese una opción válida")
                Opcion = int(input(f"""--------------- Menú Principal --------------- | #{Conteo} 
        1) 🔍 Consultar saldo 
        2) 💳 Retirar dinero 
        3) 💰 Depositar dinero 
        4) ✅ Finalizar
        ==================================================
        Seleccione una opción:
        ➤ """))
                
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    if Opcion == 1:

                print("Tu saldo actual es: ", saldo )
                print("-"*30)
                print("\n")
                historial = historial + "🔍 Consultó saldo\n"    #-------------------------------> NO SE PARA QUE FUNCIONA O NO AUN
            
    if Opcion == 2:
        while True:    
            try:
                monto_retirar = int(input("\nIngrese el monto a retirar: "))
                while monto_retirar <= 0:
                    monto_retirar = int(input("El monto a retirar debe ser mayor que cero. Ingrese un nuevo monto: "))

                if monto_retirar > saldo:   
                    print("✗ Fondos insuficientes.saldo actual: ", saldo)
                    continue
                
                if retiro_diario+monto_retirar > limite_diario_retiro:
                    disponible = limite_diario_retiro-retiro_diario
                    print(f"✗ Límite diario de retiro excedido. Disponible hoy: ${disponible:.2f}")
                    continue  
                
                saldo -= monto_retirar    
                retiro_diario += monto_retirar
                fecha_actual = datetime.date.today()
                hora_actual = time.strftime("%H:%M:%S")
                print("fecha: ",fecha_actual)
                print("hora: ",hora_actual)
                print(F"\nRetiro exitoso. Su nuevo saldo actualizado es de: {saldo}\n")
                print("limite  disponible hoy: ", limite_diario_retiro-retiro_diario)
                
                break
            except ValueError:
                print("✗ Monto inválido, ingrese un valor numerico")
            
    #breyner funcion depositar
    elif Opcion == 3:
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a depositar: "))
                    
                    if cantidad <= 0:  # bug corregido BY: JOSEPH ROMERO - el codigo original tenia "cantidad < 0" lo cual permitia depositar $0. Se corrigio a "<=0" para rechazar tambien el valor cero
                         print("Error: Ingrese un valor positivo.")
                         continue

                    saldo = saldo + cantidad
                    historial = historial + "💰 Depósito de $" + str(cantidad) + "\n"
                    print(f"\nSu nuevo saldo es de: ${saldo}")
                    
                    break
                except ValueError:
                    print("Error: Ingrese un número entero válido.")
    elif Opcion == 4:
                    print("Sesión finalizada. Gracias por usar el cajero.") # bug corregido BY: JOSEPH ROMERO - la opcion 4 no tenia funcion, ahora finaliza la sesion correctamente
                    break
print("\nGracias por usar el cajero automático")

