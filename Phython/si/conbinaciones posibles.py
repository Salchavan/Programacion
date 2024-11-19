from itertools import product
import time
#  ^--no se que es    ^--nose que es
alphabet = 'abcdefghijklmnñopqrstuvwxyz'
#entiendo esto--^
combinations = [''.join(i) for i in product(alphabet, repeat = 3)]
#no entiendo nada de nada                    ^           ^--esto es para la cantidad de digitos        
#                                            ^--esto es el alfabeto 
print(combinations)
#      ^--lista de las combinaciones
print(len(combinations))
#      ^--cantidad de combinaciones
time.sleep(100)