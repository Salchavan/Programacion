nota = 1
nota_prom = 0
aprobados = 0
reprobados = 0
examenes = 0
listado = list()

print("(Ingrese 0 para terminar)")
while(nota != 0):
    nota = int(input("Ingrese una nota: "))
    if(nota != 0):
        examenes = examenes + 1
        if(nota >= 7):
            aprobados = aprobados + 1
            nota_prom = nota_prom + nota
            listado.append ("Aprobado ", nota)
        else:
            reprobados = reprobados + 1
            nota_prom = nota_prom + nota
            listado.append ("Desaprobado ", nota)

promedio_de_notas = nota_prom / examenes * 100
promedio = aprobados / examenes * 100
print(f"La cantidad de examnes fue ▶ {examenes} ◀")
print(f"La cantidad de aprobados fue ▶ {aprobados} ◀")
print(f"La cantidad de reprobados fue ▶ {reprobados} ◀")
print(f"El promedio de aprovados de los {examenes} examenes es de ▶ {promedio}% ◀")
print(f"El promedio de nota es de ▶ {promedio_de_notas} ◀")

