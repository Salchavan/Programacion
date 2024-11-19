texto = input("Ingrese un texto: ")
texto = texto.split( )
segundos = len(texto) / 2
if segundos <= 60:
    print(f"Tardarias {segundos}s en decir esa frase")
else:
    print("Para un poco, no te pedi un testamento")
    print(f"Tardarias {segundos}s en decir esa frase")