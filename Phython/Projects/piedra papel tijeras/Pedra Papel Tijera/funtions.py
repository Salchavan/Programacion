import time
import os
import random
from turtle import *
from itertools import *

### funciones
# limpiador de terminal
def clearConsole():
    os.system("cls")

# sleep
def wait(seconds):
    time.sleep(seconds)

# menu de jugadas
def menuPlays():
    print("""-------------------------------
        Elige una jugada
-------------------------------
    1 - Piedra
    2 - Papel
    3 - Tijeras
    0 - Salir
-------------------------------""")

# opcion de modos
def menuMode():
        print("""-------------------------------
        Elige un modo
-------------------------------
    1 - Al mejor de 3
    2 - Infinito
    3 - El que llegue a 3
    0 - Salir
-------------------------------""")

# ganar o perder
def succesFailureOrTie(choise, contraChoise):
    if choise == 1:
        if contraChoise == "stone":
            return "tie"
        elif contraChoise == "paper":
            return "failure"
        elif contraChoise == "scissor":
            return "succes"
    elif choise == 2:
        if contraChoise == "stone":
            return "succes"
        elif contraChoise == "paper":
            return "tie"
        elif contraChoise == "scissor":
            return "failure"
    elif choise == 3:
        if contraChoise == "stone":
            return "failure"
        elif contraChoise == "paper":
            return "succes"
        elif contraChoise == "scissor":
            return "tie"
    elif choise == 0:
        return "exit"
    else:
        return "error"

# mostrar estadisticas
# def printScores(playerFailure, playerWin, playerDeffeat, playerSucces, playerTie, enemyWin, enemyDeffeat, enemyFailure, enemySucces, enemyTie):
#     print("""-------------------------------
#         Estadisticas
# -----------#########-----------
#             Jugador
# -------------------------------""")
#     print(f"> Victorias < ({playerWin}) >> {(playerWin / playerDeffeat) * 100}%")
#     print(f"> Derrotas < ({playerDeffeat}) >> {(playerDeffeat / playerWin) * 100}%")
#     print(f"> Exitos < ({playerSucces}) >> {(playerFailure + playerTie / playerSucces) * 100}%")
#     print(f"> Fallos < ({playerFailure}) >> {(playerSucces + playerTie / playerFailure) * 100}%")
#     print(f"> Empates < ({playerTie}) >> {(playerFailure + playerSucces) * 100}%")
#     print("""-----------#########-----------
#             Maquina
# -------------------------------""")
#     print(f"> Victorias < ({enemyWin}) >> {(enemyWin / enemyDeffeat) * 100}%")
#     print(f"> Derrotas < ({enemyDeffeat}) >> {(enemyDeffeat / enemyWin) * 100}%")
#     print(f"> Exitos < ({enemySucces}) >> {(enemyFailure + enemyTie / enemySucces) * 100}%")
#     print(f"> Fallos < ({enemyFailure}) >> {(enemySucces + enemyTie / enemyFailure) * 100}%")
#     print(f"> Empates < ({enemyTie}) >> {(enemySucces + enemyFailure / enemyTie) * 100}%")
#     print("-------------------------------")
