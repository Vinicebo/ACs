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
Número 2-
Dama
"""

def xadrez():
    while True:
        coordenadas = [int(s) for s in input().split()]
        if coordenadas[0] == 0 and coordenadas[1] == 0 and coordenadas[2] == 0 and coordenadas[3] == 0:
            break
        rainha = [coordenadas[0], coordenadas[1]]
        destino = [coordenadas[2], coordenadas[3]]
        if destino[0] == rainha[0] and destino[1] == rainha[1]:
            print("0")
            continue
        if destino[0] == rainha[0] or destino[1] == rainha[1]:
            print("1")
            continue
        if abs(destino[0] - rainha[0]) == abs(destino[1] - rainha[1]):
            print("1")
        else:
            print("2")
            continue

"""
Número 3-
Soma de fatoriais
"""
def soma_fatorial():
    while True:
        try:
            M, N = map(int, input().split())
        except EOFError:
            break
        resultadoM = 1
        resultadoN = 1
        for i in range(1, M+1):
            resultadoM *= i
        for i in range(1, N+1):
            resultadoN *= i
        print(resultadoN + resultadoM)



""" 
Número 4-
Blobs
"""
def blobs():
    N = int(input())
    for _ in range(N):
        C = float(input())
        dias = 0
        while C > 1:
            C /= 2
            dias += 1
        print(f"{dias} dias")

        
"""  
Número 5-
Frequencia de Números
"""
def frequencia_de_numero():
    N = int(input().strip())


    frequencia = {}

    # Lê cada valor de entrada
    for _ in range(N):
        X = int(input().strip())
    
        if X in frequencia:
            frequencia[X] += 1
        
        else:
            frequencia[X] = 1


    numeros_ordenados = sorted(frequencia.keys())


    for numero in numeros_ordenados:
        print(f"{numero} aparece {frequencia[numero]} vezes")

"""
Número 6-
Primo Rápido
"""

def e_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
for _ in range(N):
    X = int(input())
    print("Prime" if e_prime(X) else "Not Prime")

"""
Número 7-

"""
"""
Número 7-
Cara ou cora
"""
N = int(input())

while N != 0:
    resultados = [int(s) for s in input().split()]
    
    cara = resultados.count(0)
    coroa = resultados.count(1)
    print("Mary won {} times and John won {} times".format(cara, coroa))
    N = int(input())


