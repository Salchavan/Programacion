# imports
import os
import random
from body import playerCash

# const
cardList = [["A♥︎", "2♥︎", "3♥︎", "4♥︎", "5♥︎", "6♥︎", "7♥︎", "8♥︎", "9♥︎", "10♥︎", "J♥︎", "Q♥︎", "K♥︎"], 
            ["A♠︎", "2♠︎", "3♠︎", "4♠︎", "5♠︎", "6♠︎", "7♠︎", "8♠︎", "9♠︎", "10♠︎", "J♠︎", "Q♠︎", "K♠︎"], 
            ["A♦︎", "2♦︎", "3♦︎", "4♦︎", "5♦︎", "6♦︎", "7♦︎", "8♦︎", "9♦︎", "10♦︎", "J♦︎", "Q♦︎", "K♦︎"], 
            ["A♣︎", "2♣︎", "3♣︎", "4♣︎", "5♣︎", "6♣︎", "7♣︎", "8♣︎", "9♣︎", "10♣︎", "J♣︎", "Q♣︎", "K♣︎"]]

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
    
# plays
def menuPlays():
    print(f"""------------------------------------
|            Game
------------------------------------
|    - Your play: {startGame.playerCardListPlay}
|
|    - Dealer play: {startGame.dealerCardListPlay + startGame.loop-1*"??"}
------------------------------------
| 1- Stay  2- Ask  
------------------------------------""")
    
# card selection
def cardSelector():
    cardType = random.randint(0, 3)
    cardNumber = random.randint(0, 12)
    return cardList[cardType][cardNumber]

# start game
def startGame():
    playerCardListPlay = [cardSelector(), cardSelector()]
    dealerCardListPlay = [cardSelector(), cardSelector()]
    loop = 0
    while True:
        loop += 1
        menuPlays()
        option = int(input("Enter a option: "))
        if option == 1:
            pass
        elif option == 2:
            playerCardListPlay.append(cardSelector())