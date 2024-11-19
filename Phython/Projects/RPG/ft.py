# Here is the functions of main.py
# Created by Salvador at 24/1/2024 20:30 

# IMPORTS
import string 
import random 
import time
import os
import cls
import db

# SIMPLE FUNCTIONS
def wait(t):
    time.sleep(t)

def clear():
    os.system("cls")

# VIEW PANEL
def PLInfo(nm, lf, str, agi, wea, arm, st):
    print(f"""------------------------------------------------------------------------------
    {nm} ----> Status: [{st}]
----------------------------------------------------------------------------------
Life: [{lf}]| Strength: [{str}]| Agility: [{agi}]| Weapon: [{wea}]| Armor: [{arm}]
----------------------------------------------------------------------------------
""")
def MSTInfo(nm, lf, str, agi, wea, arm, st):
    print(f"""-------------------------------------------------
    {nm} ----> Status: [{st}]
-------------------------------------------------
Life: [{lf}]| Strength: [{str}]| Agility: [{agi}]
-------------------------------------------------
""")

# SELECT NAME
def selectName():
    def findChar(str):
        find_char = [char.isalpha() for char in str]
        return all(find_char)
    while True:
        print("No numbers or symbols, minor a 10 characters")
        name = input("What is your name?: ")
        if (len(name) > 10) or (findChar == False):
            clear()
            print(f"The name is invalid")
        elif (len(name) < 10) or (findChar == True):
            print("Done!")
            wait(2)
            clear()
            break; 
        else:
            print("ERROR selectName")
    return name

# ENEMY SELECTOR
def enemySelector():
    mst_selected = db.Monsters[random.randint(0, len(db.Monsters) - 1)]
    MSTInfo(mst_selected[0], mst_selected[1], mst_selected[2], mst_selected[3], mst_selected[4], mst_selected[5],)