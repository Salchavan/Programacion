# Here is the main code
# Created by Salvador at 24/1/2024 20:30 

# IMPORTS
import ft
import cls
import random

ft.clear()
# DECLARATIONS
PL = cls.Player(ft.selectName(), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), "normal", None, None)

# CODE
while PL.life != 0:
    ft.PLInfo(PL.name, PL.life, PL.strength, PL.agility, PL.weapon, PL.armor, PL.status)
    ft.enemySelector()





    ft.wait(5)
    ft.clear()