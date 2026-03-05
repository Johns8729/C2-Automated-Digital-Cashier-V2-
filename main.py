#(Jafet) FUNCION MENU
from time import sleep
welcome = """
╔════════════════════════════════════════════════════════════╗
                🏦 TECH BANK RIWI DIGITAL 🏦
            🙌¡Bienvenido al Cajero Automático!🙌
╚════════════════════════════════════════════════════════════╝
    """
# CONFIGURACION INICIAL, VAMOS A DETERMINAR LAS VARIABLES 
from time import sleep
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

"""Feature: Athentication Process
Made by: Oscar Corzo
Date: 2026-03-05"""

pin_correcto = 1234
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    try:
        user_pin = int(input("~ Por favor, ingrese su PIN de autenticación para continuar:\n➤ "))




        
    except:
        print("RESOLVER PROBLEMA AQUI")#-------------------------------------------------------------------------> PROBLEMA (ESTE EXCEPT ARREGLARLO, NO EXISTIA, YO LO COLOQUE)






Cant_Operaciones = int(input(f"{'¿Cuántas operaciones desea realizar?':^55}"))
while Cant_Operaciones <= 0:
    print (f"\n{'❌ Error: Ingrese un valor positivo ❌':^65}\n")
    Cant_Operaciones = int(input(f"{'¿Cuántas operaciones desea realizar?':^65}"))

for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion = int(input(f"""--------------- Menú Principal --------------- | #{Conteo} 
1) 🔍 Consultar saldo 
2) 💳 Retirar dinero 
3) 💰 Depositar dinero 
4) ✅ Finalizar
==================================================
Seleccione una opción:
➤ """))       
    while Opcion < 1 or Opcion > 4:
        print("\nERROR: Por favor ingrese una opción válida")
        Opcion = int(input(f"""--------------- Menú Principal --------------- | #{Conteo} 
1) 🔍 Consultar saldo 
2) 💳 Retirar dinero 
3) 💰 Depositar dinero 
4) ✅ Finalizar
==================================================
Seleccione una opción:
➤ """))



