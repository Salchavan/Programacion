#Programa: Trabajo practico de Ahorcado
#Autores: Salvador castellanos y Bruno Ibarra
#Fecha: 06/10/23
#Comentario: hola
from turtle import *
import time

def horca():
    pensize(7)
    pencolor("brown")
    speed(5)

    penup()
    goto(-300,0)

    pendown()
    goto(-150,0)
    penup()

    goto(-220,0)

    pendown()
    goto(-220,200)
    goto(-100,200)
    goto(-100,170)
    penup()

def head():
    pensize(3)
    pencolor("black")
    speed(5)

    goto(-100,140)

    pendown()
    circle(15)
    penup()

def body():
    pensize(3)
    pencolor("black")
    speed(1)

    pendown()
    goto(-100,70)
    penup()

def lhand():
    pensize(3)
    pencolor("black")
    speed(1)

    goto(-100,135)

    pendown()
    goto(-70,100)
    penup()
    
def rhand():
    pensize(3)
    pencolor("black")
    speed(1)

    goto(-100,135)

    pendown()
    goto(-130,100)
    penup()

def lfoot():
    pensize(3)
    pencolor("black")
    speed(1)

    goto(-100,70)

    pendown()
    goto(-120,35)
    penup()

def rfoot():
    pensize(3)
    pencolor("black")
    speed(1)

    goto(-100,70)

    pendown()
    goto(-80,35)
    penup()

def dead():
    pensize(4)
    pencolor("red")
    speed(1)

    goto(-70,137)

    pendown()
    goto(-130,137)
    penup()

horca(), head(), body(), lhand(), rhand(), lfoot(), rfoot(), dead()

time.sleep(5)
clear()
time.sleep(5)
