"""
1 - 
Aumenta salário
"""
# salario = float(input())

# if salario >= 0 and salario <= 400.00:
#     novo_salario = salario * 1.15
#     reajuste = novo_salario - salario
#     percentual = 15
# elif salario >= 400.01 and salario <= 800.00:
#     novo_salario = salario * 1.12
#     reajuste = novo_salario - salario
#     percentual = 12
# elif salario >= 800.01 and salario <= 1200.00:
#     novo_salario = salario * 1.10
#     reajuste = novo_salario - salario
#     percentual = 10
# elif salario >= 1200.01 and salario <= 2000.00:
#     novo_salario = salario * 1.07
#     reajuste = novo_salario - salario
#     percentual = 7
# elif salario > 2000.00:
#     novo_salario = salario * 1.04
#     reajuste = novo_salario - salario
#     percentual = 4
# else:
#     pass  

# print("Novo salario: {:.2f}".format(novo_salario))
# print("Reajuste ganho: {:.2f}".format(reajuste))
# print("Em percentual: {} %".format(percentual))

"""
2 -
Pares entre cinco números
"""    
# numeros = []
# for i in range(5):
#     numeros.append(int(input()))

# pares = 0
# for i in numeros:
#     if i % 2 == 0:
#         pares += 1

# print(f'{pares} valores pares')
"""
3 -
Múltiplos de 13
"""
# x = int(input())
# y = int(input())
# soma = 0

# if y > x: 
#     for i in range(x, y + 1):
#         if i % 13 != 0:
#             print(i)
#         soma += i 
        
# if x > y: 
#     for i in range(y, x + 1):
#         if i % 13 != 0:
#             print(i)
#         soma += i 

# print(soma)

"""
4 -
Preenchimento de Vetor I
"""
# V = int(input())

# if V > 50:
#     exit()
# N = [0]*10 
# N[0] = V
# for i in range(1, len(N)):
#     N[i] = N[i-1] * 2

# for i in range(len(N)):
#     print(f"N[{i}] = {N[i]}")

"""
5 - 
Menor posição
"""
# N = int(input())
# if N > 1000 or N < 1:
#     exit()

# menor = [int(s) for s in input().split()]

# menor = [int(s) for s in lista]
# menor.sort()

# print("Menor valor:", menor[0])
# print("Posicao:", lista.index(menor[0]))

""" 
6 - 
Coluna matriz
"""
# C = int(input())
# lista = []
# T = input().upper() 
# for _ in range(144):
#     lista.append(float(input()))
# soma = 0
# media = 0
# if T == "S":
#     for _ in range(0, 12):

#         soma += lista[C]
#         C += 12
#     print("{:.1f}".format(soma))
# if T == "M":
#     for _ in range(0, 12):
#         media += lista[C]
#         C += 12
#     print("{:.1f}".format(media / 12))

"""
7 -
Ordenação por Tamanho

"""

# N = int(input())

# for _ in range(1, N +1):
#     palavras = input().split()
#     palavras.sort(key=len, reverse = True)
#     print(" ".join(palavras))



    
