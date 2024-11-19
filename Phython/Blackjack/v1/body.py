# Made by Salvador Castellanos
# Started in 21/04/2024
# Ended in --/--/----
# Version: ALPHA v0.0
# Notes: 

# imports
import os
import random

# functions
# others
def clearConsole():
    os.system("cls")

# body functions
# menus
def printOptionMenu():
    print("""------------------------------------
            Option Menu
------------------------------------
    1- Play
    2- Loan
    3- Economy
    4- Record
    0- Exit
------------------------------------""")
# loan menu
def printLoanOptionMenu():
    print(f"""------------------------------------
            Loan Menu
------------------------------------
        Your Cash: ${playerCash}
------------------------------------
    1- Min Loan: $10
    2- Max Loan: ${playerCash}
    3- Custom
------------------------------------""")
    
# start game
def startGame():
    playerCardListPlay = [cardSelector(), cardSelector()]
    dealerCardListPlay = [cardSelector(), cardSelector()]
    loop = 0
    loop += 1
    def menuPlays(playerCardListPlay, dealerCardListPlay, loop):
        print(f"""------------------------------------
|            Game
------------------------------------
|    - Your play: {playerCardListPlay}
|
|    - Dealer play: {dealerCardListPlay + startGame.loop-1*"??"}
------------------------------------
| 1- Stay  2- Ask  
------------------------------------""")
    while True:
        menuPlays()
        option = int(input("Enter a option: "))
        if option == 1:
            pass
        elif option == 2:
            playerCardListPlay.append(cardSelector())
    
# card selection
def cardSelector():
    cardList = [["A♥︎", "2♥︎", "3♥︎", "4♥︎", "5♥︎", "6♥︎", "7♥︎", "8♥︎", "9♥︎", "10♥︎", "J♥︎", "Q♥︎", "K♥︎"], 
                ["A♠︎", "2♠︎", "3♠︎", "4♠︎", "5♠︎", "6♠︎", "7♠︎", "8♠︎", "9♠︎", "10♠︎", "J♠︎", "Q♠︎", "K♠︎"], 
                ["A♦︎", "2♦︎", "3♦︎", "4♦︎", "5♦︎", "6♦︎", "7♦︎", "8♦︎", "9♦︎", "10♦︎", "J♦︎", "Q♦︎", "K♦︎"], 
                ["A♣︎", "2♣︎", "3♣︎", "4♣︎", "5♣︎", "6♣︎", "7♣︎", "8♣︎", "9♣︎", "10♣︎", "J♣︎", "Q♣︎", "K♣︎"]]
    cardType = random.randint(0, 3)
    cardNumber = random.randint(0, 12)
    return cardList[cardType][cardNumber]

# const


# var
playerCash = 100
dealerCash = 10000

# body
while True:
    printOptionMenu()
    option = int(input("Enter a option: "))
    clearConsole()
    if option == 1:
        printLoanOptionMenu()
        option = int(input("Enter a option: "))
        if option == 1:
            startGame()
    elif option == 2:
        print("!! In construction")
    elif option == 3:
        print("!! In construction")
    elif option == 4:
        print("!! In construction")
    elif option == 0:
        print("Bye Bye")
        break
    else: 
        print(f'"{option}" is not an option')