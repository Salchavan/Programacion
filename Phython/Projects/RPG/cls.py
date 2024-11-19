# Here is the functions of main.py
# Created by Salvador at 24/1/2024 20:30 

# CREATURES
class Creature():
    def __init__(self, name, life, strength, agility, status):
        self.name = name
        self.life = life
        self.strength = strength
        self.agility = agility
        self.status = status
        
        def dodge(self):
            print(f"{self.name} dodged it!")

        def scape(self):
            print(f"{self.name} escaped!")

class Player(Creature):
    def __init__(self, name, life, strength, agility, status, weapon, armor):
        super().__init__(name, life, strength, agility, status)
        self.weapon = weapon
        self.armor = armor

# MONSTERS
class Monster(Creature):
    def __init__(self, name, life, strength, agility, status, specialAttack):
        super().__init__(name, life, strength, agility, status)
        self.specialAttack = specialAttack

# ITEMS
# F=x0.40 E=x0.80 D=x0.90 C=x1 B=x1.1 A=x1.3 S=x2 SR=x4
class Item():
    QF = 0.4
    QE = 0.80
    QD = 0.90
    QC = 1
    QB = 1.1
    QA = 1.3
    QS = 2
    QSR = 5
    def __init__(self, id, name, quality, durability):
        self.id = id
        self.name = name
        self.quality = quality
        self.durability = durability * quality
        

class Weapon(Item): 
    def __init__(self, id, name, durability, quality, damage):
        super().__init__(id, name, durability, quality)
        self.id = id
        self.name = name
        self.quality = quality
        self.durability = durability * quality
        self.damage = damage * quality