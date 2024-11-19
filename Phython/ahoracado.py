# Hecho por salvador castellanos
# 01/09/23

# librerias
import os
import time

# variables
vida = 6
tiene = []
no_tiene = []

# palabra secreta
palabra_secreta = str(input("Escribe la palabra secreta: ").lower())
caracteres = len(palabra_secreta)

palabra_vacia = []
for a in range(caracteres):
    palabra_vacia.append("_")
os.system("cls")

# intro
def intro():
    print("Comienza el juego en...")
    for a in range(1, 6):
        print(f"{a}s")
        time.sleep(0.1)
intro()

# intentos
while vida != 0:
    print(f"Contiene: {tiene}")
    print(f"No contiene {no_tiene}")

    intento = str(input("Ingrese una letra: "))
    acierto = palabra_secreta.count(letra)
    os.system("cls")
    if 
    if acierto > 0:
        print(f"Hubieron {acierto} aciertos ({vida}/6)")
        tiene.append(letra)
    else:
        vida -= 1
        print(f"No hubieron aciertos ({vida}/6)")
        no_tiene.append(letra)

# win or game over
if vida == 0:
    print(f"Perdiste, la palabra secreta era {palabra_secreta}")
if vida > 0:
    print(f"Ganaste!!")