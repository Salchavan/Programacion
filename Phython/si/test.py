a = int(input("Ingrese el numero a factorear: "))

def calfac(n):
    if n > 0:
        n = n * calfac(n - 1)
    else:
        n = 1
    return n

factorial_a = calfac(a)
print ("El factorial de ", a ,"es ",factorial_a)