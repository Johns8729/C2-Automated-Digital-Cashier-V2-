# BY: JOSEPH ROMERO - C2_FIX_INPUT_VALIDATION_BUGS

# ============================================================
# Bug 1 - Autentication Process
# ============================================================
else:
    max_intentos -= 1 # bug corregido BY: JOSEPH ROMERO: el codigo original tenia "intentos += 0" lo cual nunca sumaba al contador, generando un bucle infinito. Se elimino la linea redundante y se dejo solo "max_intentos -= 1" para el conteo correcto de intentos

