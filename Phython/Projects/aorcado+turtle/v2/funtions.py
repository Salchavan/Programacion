import time
import os
import random
from turtle import *
from itertools import *

## parte logica
# replace por index
def replaceIndexString(string, position, element):
    result = string[:position] + element + string[position + 1:]
    return result

# limpiador de terminal
def clearConsole():
    os.system("cls")

# sleep
def wait(seconds):
    time.sleep(seconds)

# menu final
def finalMenu():
        print("""------------------------------------
        Elige una opcion
------------------------------------
    0. Cerrar el programa
    1. Jugar de nuevo
    2. Guardar mi puntuacion
------------------------------------""")

# mostrat puntaje
def printScore():
    txt = open("data.txt", "r")
    print(txt.readlines())
    txt.close()

# guardar score
def saveScore(newScore):
    txt = open("data.txt", "w")
    txt.writelines(str(newScore))
    txt.close()


## parte grafica
# dibujar horca
def drawHorca():
    # config
    pensize(7)
    pencolor("brown")
    speed(5)

    # colocation
    penup()
    goto(-300,0)

    # draw
    pendown()
    goto(-150,0)
    penup()

    # colocation
    goto(-220,0)

    # draw
    pendown()
    goto(-220,200)
    goto(-100,200)
    goto(-100,170)
    penup()

# dibujar cabeza
def drawHead():
    # config
    pensize(3)
    pencolor("black")
    speed(5)

    # colocation
    goto(-100,140)

    # draw
    pendown()
    circle(15)
    penup()

# dibujar cuerpo
def drawBody():
    # config
    pensize(3)
    pencolor("black")
    speed(1)

    # colocation

    # draw
    pendown()
    goto(-100,70)
    penup()

# dibujar mano derecha
def drawLeftHand():
    # config
    pensize(3)
    pencolor("black")
    speed(1)

    # colocation
    goto(-100,135)

    # draw
    pendown()
    goto(-70,100)
    penup()

# dibujar mano izquierda
def drawRightHand():
    # config
    pensize(3)
    pencolor("black")
    speed(1)

    # colocation
    goto(-100,135)

    # draw
    pendown()
    goto(-130,100)
    penup()

# dibujar pierna derecha
def drawLeftFoot():
    # config
    pensize(3)
    pencolor("black")
    speed(1)

    # colocation
    goto(-100,70)

    # draw
    pendown()
    goto(-120,35)
    penup()

# dibujar pierna izquierda
def drawRigthFoot():
    # config
    pensize(3)
    pencolor("black")
    speed(1)

    # colocation
    goto(-100,70)

    # draw
    pendown()
    goto(-80,35)
    penup()

# dibujar reprecentacion de la muerte
def drawDead():
    # config
    pensize(4)
    pencolor("red")
    speed(1)

    # colocation
    goto(-70,137)

    # draw
    pendown()
    goto(-130,137)
    penup()

finalMenu()