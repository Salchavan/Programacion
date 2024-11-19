from funtions import *
clearConsole()

# declaraciones
plays = ["stone", "paper", "scissor"]
roound = 0

playerScore = 0
playerSucces = 0
playerFailure = 0
playerTie = 0
playerWin = 0
playerDeffeat = 0

enemyScore = 0
enemySucces = 0
enemyFailure = 0
enemyTie = 0
enemyWin = 0
enemyDeffeat = 0

## modos
def modeBestOf3():  
    # declaraciones
    playerScore = 0
    playerSucces = 0
    playerFailure = 0
    playerTie = 0
    playerWin = 0
    playerDeffeat = 0

    enemyScore = 0
    enemySucces = 0
    enemyFailure = 0
    enemyTie = 0
    enemyWin = 0
    enemyDeffeat = 0
    roound = 0
    # juego
    while True:
        # header
        print(f"Ronda {roound} de 3")
        print("Scores >> Jugador = ", "|" * playerScore)
        print("Scores >> Computadora = ", "|" * enemyScore)
        menuPlays()
        playerChoise = int(input("Ingrese una opcion: "))
        enemyChoise = random.choice(plays)
        clearConsole()
        # exito o fallo
        if succesFailureOrTie(playerChoise, enemyChoise) == "succes":
            print("Ganaste!!")
            playerScore += 1
            playerSucces += 1
        elif succesFailureOrTie(playerChoise, enemyChoise) == "failure":
            print("Perdiste")
            enemyScore += 1
            playerFailure += 1
        elif succesFailureOrTie(playerChoise, enemyChoise) == "tie":
            print("Empataste!!")
            playerTie += 1
            roound -= 1
        elif succesFailureOrTie(playerChoise, enemyChoise) == "exit":
            break
        elif succesFailureOrTie(playerChoise, enemyChoise) == "error":
            print("Opcion no valida")
            
        if playerScore == 2:
            clearConsole()
            print("Ganaste la partida!!")
            break
        elif enemyScore == 2:
            clearConsole()
            print("Perdiste la partida!!")
            break

        roound += 1

    return playerFailure, playerWin, playerDeffeat, playerSucces, playerTie, enemyWin, enemyDeffeat, enemyFailure, enemySucces, enemyTie
    
def modeInfinite():
    # declaraciones
    playerScore = 0
    playerSucces = 0
    playerFailure = 0
    playerTie = 0
    playerWin = 0
    playerDeffeat = 0

    enemyScore = 0
    enemySucces = 0
    enemyFailure = 0
    enemyTie = 0
    enemyWin = 0
    enemyDeffeat = 0
    #juego
    while end != True:
        # header
        print(f"Ronda {roound}")
        print("Scores >> Jugador = ", "|" * playerScore, f"({playerScore})")
        print("Scores >> Computadora = ", "|" * enemyScore, f"({enemyScore})")
        menuPlays()
        playerChoise = int(input("Ingrese una opcion: "))
        enemyChoise = random.choice(plays)
        clearConsole()
        # exito o fallo
        if succesFailureOrTie(playerChoise, enemyChoise) == "succes":
            print("Ganaste!!")
            playerScore += 1
            playerSucces += 1
        elif succesFailureOrTie(playerChoise, enemyChoise) == "failure":
            print("Perdiste")
            enemyScore += 1
            playerFailure += 1
        elif succesFailureOrTie(playerChoise, enemyChoise) == "tie":
            print("Empataste!!")
            playerTie += 1
        elif succesFailureOrTie(playerChoise, enemyChoise) == "exit":
            break
        elif succesFailureOrTie(playerChoise, enemyChoise) == "error":
            print("Opcion no valida")

        roound += 1
    return playerFailure, playerWin, playerDeffeat, playerSucces, playerTie, enemyWin, enemyDeffeat, enemyFailure, enemySucces, enemyTie


def modeAt3():
    # declaraciones
    playerScore = 0
    playerSucces = 0
    playerFailure = 0
    playerTie = 0
    playerWin = 0
    playerDeffeat = 0

    enemyScore = 0
    enemySucces = 0
    enemyFailure = 0
    enemyTie = 0
    enemyWin = 0
    enemyDeffeat = 0
    while end != True:
        # declaraciones
        roound = 0
        #juego
        while True:
            # header
            print(f"Ronda {roound}")
            print("Scores >> Jugador = ", "|" * playerScore, f"({playerScore})")
            print("Scores >> Computadora = ", "|" * enemyScore, f"({enemyScore})")
            menuPlays()
            playerChoise = int(input("Ingrese una opcion: "))
            enemyChoise = random.choice(plays)
            clearConsole()
            # exito o fallo
            if succesFailureOrTie(playerChoise, enemyChoise) == "succes":
                print("Ganaste!!")
                playerScore += 1
                playerSucces += 1
            elif succesFailureOrTie(playerChoise, enemyChoise) == "failure":
                print("Perdiste")
                enemyScore += 1
                playerFailure += 1
            elif succesFailureOrTie(playerChoise, enemyChoise) == "tie":
                print("Empataste!!")
                playerTie += 1
            elif succesFailureOrTie(playerChoise, enemyChoise) == "exit":
                break
            elif succesFailureOrTie(playerChoise, enemyChoise) == "error":
                print("Opcion no valida")

            if playerScore == 3:
                clearConsole()
                print("Ganaste la partida!!")
                break
            elif enemyScore == 3:
                clearConsole()
                print("Perdiste la partida!!")
                break

            roound += 1

        if playerScore == 3 or enemyScore == 3:
            break
    return playerFailure, playerWin, playerDeffeat, playerSucces, playerTie, enemyWin, enemyDeffeat, enemyFailure, enemySucces, enemyTie

            
## juego
while True:
    menuMode()
    modeChoise = int(input("ingrese una opcion: "))
    clearConsole()

    if modeChoise == 1:
        modeBestOf3()
    elif modeChoise == 2:
        modeInfinite()
    elif modeChoise == 3:
        modeAt3()
    # elif modeChoise == 4:
    #     # printScores(playerFailure, playerWin, playerDeffeat, playerSucces, playerTie, enemyWin, enemyDeffeat, enemyFailure, enemySucces, enemyTie)
    #     print("# insertar tabla de puntajes")
    elif modeChoise == 0:
        print("Hasta la proxima!!")
        break
    else:
        print("No es una opcion valida")