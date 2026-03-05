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
