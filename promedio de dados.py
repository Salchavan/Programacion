import os
teclado = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]}{|;:',.<>/?`~ "
os.system("cls")
while True:
    total = 0
    dice = str(input("Dado de cuantas caras?: "))
    if dice == "cls":
        os.system("cls")
        print("Limpio!!")
    elif teclado.find(dice) != 1:
        for i in range(1, int(dice) + 1):
            print(f"{i} + {total} = {i + total}")
            total += i
        print(f"El promedio es {total / int(dice)}")
    else:
        print("No es un numero")