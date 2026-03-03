# CONDICIONES DE RETIRO

def VALIDACION_RETIRO(saldo, monto):
    if monto <= 0:
        return False, "El monto debe ser mayor que cero!."
    if monto > saldo:
        return False, "Fondos insuficientes!."
    if monto > 1000:
        return False, "Supera el limite permitido!."
    return True, "Retiro valido"


# CONDICIONES DE DEPOSITO

def VALIDACION_DEPOSITO(monto):
    if monto <= 0:
        return False, "No se permiten montos negativos o cero"
    return True, "Depòsito Valido!."

