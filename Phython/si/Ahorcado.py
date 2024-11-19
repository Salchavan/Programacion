import os

palabrax = str(input("Ingrese la palabra secreta: "))
palabrax_list = list(palabrax)

print("(Concejo: Si ingresas una palabra arriegas todo)")
intento = input("Ingresa una letra o palabra: ")

while(intento == palabrax):
    intento = input("Ingresa una letra o palabra: ")

    if(intento in palabrax_list):
        print("Acertaste, contiene ", intento)
    else:
        print("""A la Primera!!
        La palabra era """, palabrax)
