"""Feature: Athentication Process
Made by: Oscar Corzo
Date: 2026-03-05"""

pin_correcto = 1234
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    try:
        user_pin = int(input("~ Por favor, ingrese su PIN de autenticación para continuar:\n➤ "))
