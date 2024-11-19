#datos
curso_min = 2.5
curso_prom = 4
curso_max = 7
curso_dalto = 1.5

crudo_prom = 5
crudo_dalto = 3.5

#el -100 es para ver la diferencia
print("----------------------------")
print(f"min {round(100 - curso_dalto / curso_min * 100 , 2)}%")
print(f"prom {round(100 - curso_dalto / curso_prom * 100 , 2)}%")
print(f"max {round(100 - curso_dalto / curso_max * 100 , 2)}%")
print("----------------------------")
print(f"se reduce un {round(100 - curso_dalto / crudo_dalto * 100)}% en el de dalto")
print(f"se reduce un {round(100 - curso_prom / crudo_prom * 100)}% en el prom")
print("----------------------------")
print(f"ver 10hs del curso de dalto equivale a ver {round(curso_min / curso_dalto * 10 , 2)}hs del min")
print(f"ver 10hs del curso de dalto equivale a ver {round(curso_prom / curso_dalto * 10 , 2)}hs del prom")
print(f"ver 10hs del curso de dalto equivale a ver {round(curso_max / curso_dalto * 10 , 2)}hs del max")
print("----------------------------")