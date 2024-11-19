import time
numero = int(input("Ingrese un numero: "))
data = numero
par = data % 2 == 0 
lista = []
pares = 0
inpares = 0
ciclos = 0
combospar = 0
combosinpar = 0

while data != 1:
    ciclos = ciclos + 1
    if data % 2 == 0:
        pares = pares + 1
        print(f"{data} es par dividir por 2")
        lista.append(f"{data} < par")
        data = data // 2
        if par == True:
            combospar = combospar + 1
        else: 
            combospar = 0
        par = True
        time.sleep(0.1)
    else:
        inpares = inpares + 1
        print(f"{data} es inpar multiplicar por 3 y sumnado 1")
        lista.append(f"{data} < inpar")
        data = data * 3 + 1
        if par == True:
            combosinpar = combosinpar + 1
        else: 
            combosinpar = 0
        par = False
        time.sleep(0.1)

print("Registro: ", lista)
print(f"Termino en {ciclos} siclos")
print(f"Hubo {pares} pares e {inpares} inpares")
if combospar > 0:
    print(f"El mayor combo fue de pares con {combospar + 1}")
else:
    print(f"El mayor combo fue de inpares con {combosinpar + 1}")
time.sleep(2)