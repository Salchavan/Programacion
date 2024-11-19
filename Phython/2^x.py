import time
# 1Bit
# 16Bits = 1Kb
# 1024Kb = 1Mb
# 1024Mb = 1Gb


def formatear_con_puntos(cadena):
    if not cadena.isdigit():
        return "La cadena debe contener solo dígitos."

    longitud = len(cadena)
    grupos = []

    # Dividir la cadena en grupos de tres desde atrás hacia adelante
    while longitud > 0:
        grupos.insert(0, cadena[max(longitud - 3, 0):longitud])
        longitud -= 3

    # Unir los grupos con puntos y devolver el resultado
    resultado = '.'.join(grupos)
    return resultado

def converged(n):
    n_kb = n / 16
    for unit in range(4):
        if n_kb > 1:
            n_converged = n_kb / 1024

    return n_converged

for i in range(17):
    num = 2 ** i
    num_spaced = formatear_con_puntos(str(num))
    print(f"2 ^ {i} = {num_spaced}")
    num_converged = converged(num)
    print(f"^-- = {num_converged}")
    # time.sleep(0.5)