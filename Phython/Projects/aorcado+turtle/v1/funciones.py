import time
import time
import os
from itertools import *

# replace para list
def replaceList(list, position, element):
        list.pop(position)
        return list.insert(position, element)
# palabraOculta.pop(palabraSecrete.count(intento))
# palabraOculta.insert(palabraSecrete.count(intento), intento)

# index para list
def indexList(list, element):
    if list.count(element) != 0:
        return True
    else:
        return False

# limpiador de terminal
def clearConsole():
    os.system("cls")

# sleep
def wait(seconds):
    time.sleep(seconds)
