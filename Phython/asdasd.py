import random
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
history = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0
r9 = 0
r10 = 0
r11 = 0
r12 = 0
r13 = 0
r14 = 0
r15 = 0
r16 = 0
r17 = 0
r18 = 0
r19 = 0
r20 = 0



while True:
    history = 0
    cant = int(input("Cuantas veces?: "))
    for i in range(cant):
        result = random.choice(d20)
        history.append(result)

        print(result)
    print(history)