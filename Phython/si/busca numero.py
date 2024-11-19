numerox = int(input("Ingrese el numero secreto: "))
win = False
defeat = False
registro = list()
par = False
vidas = 3

print("""
""")
par = numerox % 2 == 0

while True:
    intento = int(input("Ingrese un numero: "))
    registro.append (intento)
    if (intento == numerox):
        print("A la primera!! el numero era ", numerox)
        victoria = True
    else:
        vidas = vidas - 1
        print("Error -1 vida", f"({vidas}/3)")
        if (vidas == 0):
            print("Se te acabaron las vidas as PERDIDO")
            print("El numero era ", numerox)
        else:
            if (par == True):
                print("Pista, es par")
            else:
                print("Pista, es inpar")
        











    
