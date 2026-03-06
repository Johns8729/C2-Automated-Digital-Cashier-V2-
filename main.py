# BY: JOSEPH ROMERO - C2_FIX_INPUT_VALIDATION_BUGS

# ============================================================
# Bug 1 - Autentication Process
# ============================================================
else:
    max_intentos -= 1 # bug corregido BY: JOSEPH ROMERO: el codigo original tenia "intentos += 0" lo cual nunca sumaba al contador, generando un bucle infinito. Se elimino la linea redundante y se dejo solo "max_intentos -= 1" para el conteo correcto de intentos

# ============================================================
# Bug 2 - Deposito - linea 97
# ============================================================
if cantidad <= 0: # bug corregido BY: JOSEPH ROMERO - linea 97: el codigo original tenia "cantidad < 0" lo cual permitia depositar $0 como valor valido. Se corrigio a "cantidad <= 0" para rechazar tambien el valor cero
    print("Error: Ingrese un valor positivo.")
    continue