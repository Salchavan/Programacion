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

# Ejemplo de uso
cadena_numerica = "321425654"
cadena_formateada = formatear_con_puntos(cadena_numerica)
print(cadena_formateada)
