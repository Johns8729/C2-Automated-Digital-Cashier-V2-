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
pin_correcto = 1234
intentos_maximos = 3 
sesion_activa = False
intentos = 0 
cuenta_1 = 1234
limite_diario_retiro=800 
retiro_diario=0
monto = 0
historial = ""
max_intentos = 3
cuenta_1 = input("🤵 Ingrese su Nombre de Usuario: ")

"""Feature: Athentication Process and Attempts Control
Made by: Oscar Corzo y Valery Avila
Date: 2026-03-05"""

while intentos < max_intentos:
    try:
        user_pin = int(input(f"~ Hola {cuenta_1}!, \nPor favor ingrese su PIN de autenticación para continuar:\n➤ "))
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
    print ("Programa suspendido por demasiados intentos fallidos. Por favor, intente nuevamente más tarde.")
    exit ()

Cant_Operaciones = 0
while Cant_Operaciones <= 0:
    try:
        Cant_Operaciones= int(input (f"{'¿Cuántas operaciones desea realizar?':^62}\n➤ "))

        if Cant_Operaciones <=0:
             print("="*60)
             print(f"{'❌ Error: Ingrese un valor positivo. ❌':^65}")
             print("="*60)

    except ValueError:
         print("="*60)
         print(f"{'❌ Error: Ingrese un número entero válido. ❌':^65}")         
         print("="*60)

for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion= 0
    while Opcion <= 0:
        try:              
            Opcion = int(input(f"""---------------------- Menú Principal ---------------------- | #{Conteo} 
1) 🔍 Consultar saldo 
2) 💳 Retirar dinero 
3) 💰 Depositar dinero 
4) ✅ Finalizar
============================================================
Seleccione una opción:
➤ """)) 
            if Opcion == 0:
                print(f"\n{'❌ Error: Ingrese un valor positivo ❌':^65}\n")  

            if Opcion < 1 or Opcion > 4:
                print(f"\n{'❌ Error: Por favor ingrese una opción válida ❌':^65}\n")
                Opcion = int(input(f"""---------------------- Menú Principal ---------------------- | #{Conteo} 
1) 🔍 Consultar saldo 
2) 💳 Retirar dinero 
3) 💰 Depositar dinero 
4) ✅ Finalizar
============================================================
Seleccione una opción:
➤ """))
                
        except ValueError:
            print(f"\n{'❌ Error: Ingrese un número entero válido. ❌':^65}\n")

    if Opcion == 1:
                print("-"*60)
                print("Tu saldo actual es: ", saldo )
                print("-"*60)
                print("\n")
                historial = historial + "🔍 Consultó saldo\n"    
            
    if Opcion == 2:
        while True:    
            try:
                print("-"*60)
                monto_retirar = int(input("Ingrese el monto a retirar: "))
                while monto_retirar <= 0:
                    monto_retirar = int(input("El monto a retirar debe ser mayor que cero. Ingrese un nuevo monto: "))

                if monto_retirar > saldo:   
                    print("✗ Fondos insuficientes. Su saldo actual es de: ", saldo)
                    continue
                
                if retiro_diario+monto_retirar > limite_diario_retiro:
                    disponible = limite_diario_retiro-retiro_diario
                    print(f"✗ Límite diario de retiro excedido. Disponible hoy: ${disponible:.2f}")
                    continue  
                
                saldo -= monto_retirar
                historial = historial + "💳 Retiro de $" + str(monto_retirar) + "\n"    
                retiro_diario += monto_retirar
                fecha_actual = datetime.date.today()
                hora_actual = time.strftime("%H:%M:%S")
                print("fecha: ",fecha_actual)
                print("hora: ",hora_actual)
                print(F"\nRetiro exitoso. Su nuevo saldo actualizado es de: {saldo}\n")
                print("limite  disponible hoy: ", limite_diario_retiro-retiro_diario)
                print("-"*60,"\n")
                break
            except ValueError:
                print("✗ Monto inválido, ingrese un valor numerico")
            
    #breyner funcion depositar
    elif Opcion == 3:
            while True:
                try:
                    print("-"*60)
                    cantidad = int(input("Ingrese la cantidad a depositar: "))
                    
                    if cantidad < 0:
                         print("Error: Ingrese un valor positivo.")
                         continue

                    saldo = saldo + cantidad
                    historial = historial + "💰 Depósito de $" + str(cantidad) + "\n"
                    print(f"\nSu nuevo saldo es de: ${saldo}")
                    print("-"*60,"\n")
                    break
                except ValueError:
                    print("Error: Ingrese un número entero válido.")

#Historial de operaciones - Leonardo Perez

print(f"\n🗂️  Historial de operaciones :")

if historial == "":
    print("❌ No se realizaron operaciones ❌")
else:
    print(f"""============================================================
🤵 Usuario: {cuenta_1}
{historial}============================================================""")

print(f"Gracias {cuenta_1}, por usar el cajero automático")
