import datetime
import time
saldo = 2000
limite_diario_retiro=1500
retiro_diario=0

print("="*50)
print(f"{'🏦 TECH BANK RIWI DIGITAL':^50}")
print("-"*50)
print(f"{'🙌¡Bienvenido al Cajero Automático!🙌':^50}")
print("-"*50)
Cant_Operaciones = int(input(f"{'¿Cuántas operaciones desea realizar?':^50}"))
for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion = int(input(f"\n --------------- Menú Principal --------------- | #{Conteo}  \n 1) 🔍 Consultar saldo \n 2) 💳 Retirar dinero \n 3) 💰 Depositar dinero \n 4) ✅ Finalizar\n==================================================\n Seleccione una opción \n ➤ "))
    while Opcion < 1 or Opcion > 4:
        print("\nERROR: Por favor ingrese una opción válida")
        Opcion = int(input(f"\n --------------- Menú Principal --------------- | #{Conteo}  \n 1) 🔍 Consultar saldo \n 2) 💳 Retirar dinero \n 3) 💰 Depositar dinero \n 4) ✅ Finalizar \n==================================================\n Seleccione una opción \n ➤ "))
    if Opcion == 1:
        fecha_actual = datetime.date.today()
        hora_actual = time.strftime("%H:%M:%S")
        print("fecha: ",fecha_actual)
        print("hora: ",hora_actual)
        print("Tu saldo actual es: ", saldo )
        print("retiro relizados hoy: ", retiro_diario)
        print("retiro diario disponible hoy: ", limite_diario_retiro-retiro_diario)
        print("-"*30)
        print("\n")


    if Opcion == 2:
            try:
                monto_retirar = int(input("\ningrese el monto a retirar: "))
             
                while monto_retirar <= 0:
                    monto_retirar = int(input("El monto a retirar debe ser mayor que cero.Ingrese un nuevo monto: "))

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
                print("\nGracias por usar el cajero automático")
                

            except ValueError:
                print("✗ Monto inválido")
                
                    
                
            
