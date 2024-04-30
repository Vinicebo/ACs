"""
Atividade 1-
Figurinhas
"""
def mdc():
    N = int(input())

    for _ in range (N):
        numeros = [int(s) for s in input().split()]
        numeros.sort()
        f1 = numeros[1]
        f2 = numeros[0]

        resto = f1 % f2
        while resto != 0:
            f1 = f2
            f2 = resto 
            resto = f1 % f2
        print(f2)
    
mdc()

"""
Numero 2-
Damas
"""

       
