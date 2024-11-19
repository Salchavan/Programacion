# Made by Salvador Castellanos
# Started in 22/04/2024
# Ended in --/--/----
# Version: ALPHA v0.0
# Notes: second intent

# imports
import os
import random

# functions 
def cardSelector():
    cardList = [["A♥︎", "2♥︎", "3♥︎", "4♥︎", "5♥︎", "6♥︎", "7♥︎", "8♥︎", "9♥︎", "10♥︎", "J♥︎", "Q♥︎", "K♥︎"], 
                ["A♠︎", "2♠︎", "3♠︎", "4♠︎", "5♠︎", "6♠︎", "7♠︎", "8♠︎", "9♠︎", "10♠︎", "J♠︎", "Q♠︎", "K♠︎"], 
                ["A♦︎", "2♦︎", "3♦︎", "4♦︎", "5♦︎", "6♦︎", "7♦︎", "8♦︎", "9♦︎", "10♦︎", "J♦︎", "Q♦︎", "K♦︎"], 
                ["A♣︎", "2♣︎", "3♣︎", "4♣︎", "5♣︎", "6♣︎", "7♣︎", "8♣︎", "9♣︎", "10♣︎", "J♣︎", "Q♣︎", "K♣︎"]]
    cardType = random.randint(0, 3)
    cardNumber = random.randint(0, 12)
    return cardList[cardType][cardNumber]

# var
loop = 0

# game
while True:
    loop += 1
    if loop == 1:
        playerPlay = [cardSelector(), cardSelector()]
        dealerPlay = [cardSelector(), cardSelector()]
    elif loop > 1:
        pass
    else:
        print("!! Error")
    print(f"""------------------------------------
|            Game
------------------------------------
|    - Your play: {str(playerPlay)}
|
|    - Dealer play: {str(dealerPlay) + ((loop-1)*"[??]")}
------------------------------------
| 1- Stay  2- Ask  
------------------------------------""")
    option = int(input("Enter a option: "))
    if option == 1:
        pass
    elif option == 2:
        playerPlay.append(cardSelector())
