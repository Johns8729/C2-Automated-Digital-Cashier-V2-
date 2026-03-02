saldo = 1000
print("="*50)
print(f"{'🏦 BANCO DYMADOM':^50}")
print("-"*50)
print(f"{'👋🏻¡Bienvenido al Cajero Automático! 👋🏻':^50}")
print(f"saldo actual: ${saldo}")
print("-"*50)
Cant_Operaciones = int(input(f"{'¿Cuántas operaciones desea realizar?':^50}"))
for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion = int(input(f"\n --------------- Menú Principal --------------- | #{Conteo}  \n 1) Consultar saldo \n 2) Retirar dinero \n 3) Depositar dinero \n 4) Finalizar\n==================================================\n Seleccione una opción \n ➤ "))
    while Opcion < 1 or Opcion > 4:
        print("\nERROR: Por favor ingrese una opción válida")
        Opcion = int(input(f"\n --------------- Menú Principal --------------- | #{Conteo}  \n 1) Consultar saldo \n 2) Retirar dinero \n 3) Depositar dinero \n 4) Finalizar \n==================================================\n Seleccione una opción \n ➤ "))
