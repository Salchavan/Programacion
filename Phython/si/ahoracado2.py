# head
import os
import time
palabrax = str(input("""(Solo una palabra sin espacios o caracteres especiales)
Ingrese la palabra secreta: """))
vidas = 6
victoria = False
capichi = 0
palabraylist = []

# lower y list
palabraxlow = palabrax.lower()
palabraxlist = list(palabraxlow)
palabraylist = palabraxlow.replace(palabraxlow,"_")
palabraylist = list(palabraylist)


# limpia la pantalla
os.system("cls")

# prueba
print(palabraxlow)
print(palabraylist)

# reglas
# print("""REGLAS BASICAS
# > Solo carecteres del alfaveto (ej. a, b, c, etc)
# > No modificar el codigo, sino que chiste tiene el juego
# > Solo escribir una letra por intento, si colocas mas arriesgas las 6 vidas
# """)

# verificacion de las reglas
# while capichi != "true":
#     capichi = str(input("Capichi o no capichi? (True/False)"))
#     capichi = capichi.lower()
#     if capichi == "true":
#         print("Bien! Ahora comienza el juego!")
#     else:
#         print("Lee las reglas de nuevo")

# info de la palabra


# acierto o no
while (vidas != 1) or (victoria == True):
    intento = str(input("Ingrese una letra o palabra: "))
    bien = palabraxlow.find(intento)
    if bien > -1:
        print("Le acertaste")
        palabraylist.insert(bien, intento)
        print("Palabra:", palabraylist)
    else:
        print("No le acertaste")


