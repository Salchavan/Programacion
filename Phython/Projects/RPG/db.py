# Here is the functions of main.py
# Created by Salvador at 26/1/2024 11:50 

# IMPORTS
import cls
import random
import ft
# Monsters
Monsters = {
    0 : cls.Monster("Wolf", random.randint(10, 15), random.randint(5, 10), random.randint(10, 20), "normal", "bite"),
    1 : cls.Monster("Goblin", random.randint(5, 15), random.randint(5, 10), random.randint(5, 10), "normal", "provoke")
}