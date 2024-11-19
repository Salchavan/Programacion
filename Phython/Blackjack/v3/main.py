# Made by Salvador Castellanos
# Started in 22/04/2024
# Ended in --/--/----
# Version: ALPHA v0.0
# Notes: third intent

# imports
import random
import os

# functions
def cardSelector():
    card = random.randint(1, 12)
    return card
def clearConsole():
    os.system("cls")

# var
loop = 0

# body
while True:
    loop += 1
    if loop == 1:
        playerPlay = [cardSelector(), cardSelector()]
        dealerPlay = [cardSelector(), cardSelector()]
        playerCount = sum(playerPlay)
        dealerCount = sum(dealerPlay)
    elif loop > 1:
        pass
    clearConsole()
    print(f"""------------------------------------
        Your cards : {playerPlay}
------------------------------------
        Dealer cards : {dealerPlay}
------------------------------------""")
    if playerCount > 21:
        print("You Lost!")
        break
    elif dealerCount > 21:
        print("You won!")
        break

    option = int(input("[1-Stay | 2-Ask] Enter a option: "))
    if option == 1:
        pass
    elif option == 2:
        playerPlay.append(cardSelector())
        playerCount = sum(playerPlay)
