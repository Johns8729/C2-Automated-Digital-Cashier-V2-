"""Feature: attemtps control draft
Made by: Valery Avila Ortega"""

saldo = 1000
pin = 1243

print ("Cuenta con tres intentos para ingresar el pin adecuado")
contador = 1
while contador <= 3:
    pin = int (input("Ingrese su pin:"))
    if pin == 1234:
        print ("Puede continuar.")
    else:
        print ("Pin incorrecto")
        if contador == 3:
            print ("Programa suspendido.")
            print ("¿Tiene problemas con su pin? Comuniquese con nuestros asesores para más información.")
        contador = contador +1

