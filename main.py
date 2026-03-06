# BY: JOSEPH ROMERO - C2_FIX_INPUT_VALIDATION_BUGS

# ============================================================
# Bug 1 - Autentication Process
# ============================================================
else:
    max_intentos -= 1 # bug corregido BY: JOSEPH ROMERO: el codigo original tenia "intentos += 0" lo cual nunca sumaba al contador, generando un bucle infinito. Se elimino la linea redundante y se dejo solo "max_intentos -= 1" para el conteo correcto de intentos

# ============================================================
# Bug 2 - Deposit Process
# ============================================================
if cantidad <= 0: # bug corregido BY: JOSEPH ROMERO: el codigo original tenia "cantidad < 0" lo cual permitia depositar $0 como valor valido. Se corrigio a "cantidad <= 0" para rechazar tambien el valor cero
    print("Error: Ingrese un valor positivo.")
    continue

# ============================================================
# Bug 3 - Opcion 4 - exit menu
# ============================================================
elif Opcion == 4:
    print("Sesión finalizada. Gracias por usar el cajero.") # bug corregido BY: JOSEPH ROMERO: el codigo original no tenia implementada la opcion 4 del menu, al seleccionarla no ocurria nada. Se agrego mensaje de salida y "break" para finalizar correctamente la sesion
    break