# imports
from itertools import count
from funciones import *

# declaraciones
palabraSecrete = list(input("Escriba la palabra secreta: "))
numeroDeLetras = len(palabraSecrete)
os.system("cls")

# funciones

# adivinacion
palabraOculta = list(numeroDeLetras * "_")
palabraOculta.insert(0, ">> ")
for i in range(7):
    # header
    print(f"Tiene {7 - i} intentos")
    print(f"La palabra tiene {numeroDeLetras} de letras")
    print(palabraOculta)

    # intentos
    intento = str(input("Ingrese su letra a comprobar: "))
    shot = indexList(palabraSecrete, intento)

    if shot == True:
        replaceList(palabraOculta, palabraSecrete.count(intento), intento)
        print("Si contiene!")
    elif shot == False:
        print(f"> {intento} < no se encuntra en la palabra")


    wait(1)
    clearConsole()