numero = int(input("Escriba un numero: "))
ciclos = 0
lista = list()
if(numero % 2 == 0):
    lista.append (f"Par > {numero}")
else:
    lista.append (f"Inpar > {numero}")
while numero != 1:
    if(numero % 2 == 0):
        print("Par A")
        numero = numero / 2
        print(numero)
        ciclos = ciclos + 1
        lista.append (f"Par > {numero}")
    else:
        print("Inpar A")
        numero = numero * 3 + 1
        print(numero)
        ciclos = ciclos + 1
        lista.append (f"Inpar > {numero}")

print(f"Termino despues de {ciclos} siclos")
print("Lista: ", lista)

