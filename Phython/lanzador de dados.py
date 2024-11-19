import random

history = []
result = 0
d4 = [1, 2, 3, 4]
d6 = [1, 2, 3, 4, 5, 6]
d8 = [1, 2, 3, 4, 5, 6, 7, 8]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while True:
    dice = str(input("Que dado desea tirar?: "))
    cant = int(input("Cuantas veces?: "))
    if dice == "d4":
        for i in range(cant):
            result = random.choice(d4)
            history.append(result)
            print(result)
    if dice == "d6":
        for i in range(cant):
            result = random.choice(d6)
            history.append(result)
            print(result)
    if dice == "d8":
        for i in range(cant):
            result = random.choice(d8)
            history.append(result)
            print(result)
    if dice == "d10":
        for i in range(cant):
            result = random.choice(d10)
            history.append(result)
            print(result)
    if dice == "d12":
        for i in range(cant):
            result = random.choice(d12)
            history.append(result)
            print(result)
    if dice == "d20":
        for i in range(cant):
            result = random.choice(d20)
            history.append(result)
            print(result)

    print(history)