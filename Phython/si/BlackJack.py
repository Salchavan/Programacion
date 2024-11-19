limit = 21
j = 10
q = 10
k = 10
a = 1 or 11
cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, k, a]


print("""> Tus cartas <

""")

print("""---------------
1. Pedir
2. Plantarse
---------------""")
opcion = int(input("Opcion: "))


if  opcion == 1:
    print("Quiero!")
elif opcion == 2:
    print("Me planto")
elif opcion == 69:
    print("Nice, pero no es una opcion")
else:
    print("Eso no es una opcion")