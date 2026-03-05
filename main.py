#(Jafet) FUNCION MENU
from time import sleep
welcome = """
╔════════════════════════════════════════════════════════════╗
                🏦 TECH BANK RIWI DIGITAL 🏦
            🙌¡Bienvenido al Cajero Automático!🙌
╚════════════════════════════════════════════════════════════╝
    """
for _ in welcome:
    print(_,end="",flush=True)
    sleep(0.005)

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
