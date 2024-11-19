import random 
import time
import os

tiempo = 0
animales = ["perro", "gato", "Pez", "ballena", "medusa", "cucaracha"]

print("PERSONALIZEMOS!!")

while True:
    tiempo = int(input("Cuanto tiempo deseas para adivinar?(Segundos): "))
    if tiempo < 15:
        print("Numero muy bajo, solo 15 hasta 1800")
    elif tiempo > 1800:
        print("Numero muy alto, solo 15 hasta 1800")
    else:
        break


    
        
















print("EL PROGRAMA FINALIZO")