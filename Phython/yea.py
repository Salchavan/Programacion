import random

# Inicializamos un diccionario para almacenar las ocurrencias de cada número.
ocurrencias = {}
print("Iniciando...")

# Generamos 100 números aleatorios del 1 al 20.
for _ in range(10000):
    numero = random.randint(1, 20)
    
    # Comprobamos si el número ya está en el diccionario.
    if numero in ocurrencias:
        ocurrencias[numero] += 1
    else:
        ocurrencias[numero] = 1

# Mostramos el resultado.
for numero, cantidad in ocurrencias.items():
    print(f"{numero}: {cantidad} veces ({((cantidad / 10000) * 100)}% | {(((cantidad / 10000) * 100) - 5)}%)")





