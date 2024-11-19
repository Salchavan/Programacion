import random
import os
import time

cont = 0
nums = 0

def ramdom(a):
    cont = 0
    nums = ""
    while cont != a:
        n = random.randint(0, 9)
        nums = nums + str(n)
        cont += 1
    print(nums)
    cont = 0

os.system("cls")
option = int(input("Queres codigos nucleares? (1.Si / 0.No): "))
os.system("cls")

while option != 0:
    if option == 1:
        cuantos = int(input("Cuantos codigos? : "))
        os.system("cls")
        if cuantos > 0:
            tamaño = int(input("De cuantos digitos? : "))
            os.system("cls")
            if tamaño > 0:
                while cuantos != 0:
                    cont += 1
                    print(f"{cont})")
                    ramdom(tamaño)
                    cuantos -= 1
                cont = 0
            else:
                print("Ese no es un numero posible")
        else:
            print("Ese no es un numero posible")
    elif option != 1 and option != 0:
        print("No es una opcion")

    option = int(input("""
    (Si aceptas se borraran los anteriores)
    Queres otro codigo nuclear (1.Si / 0.No): """))
    if option == 1:
        os.system("cls")

if option == 0:
    os.system("cls")
    print("Okay :(")
    time.sleep(3)
