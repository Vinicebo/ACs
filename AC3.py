"""
Exercício 1: triângulos
Desenvolva uma função determina_tipo_triangulo que recebe três lados de um triângulo e retorna uma string, "Escaleno", 
"Isósceles" ou "Equilátero", conforme o tipo do triângulo. A função deve retornar "Não é um triângulo" se os três lados não formarem um triângulo. 
"""
def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Não existe'
    elif a == b == c:
        return 'Equilátero'
    elif a == b or b == c:
        return 'Isósceles'
    else:
        return 'Escaleno'


print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que recebe um número inteiro
e retorna uma string indicando o dia da semana equivalente, considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc.
A função deve retornar uma string vazia caso o número seja inválido. Use a função abaixo como teste:
"""
def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira" 
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return ""
    
print(dia_semana(1))
print(dia_semana(2))
print(dia_semana(4))
print(dia_semana(5))
print(dia_semana(6))
print(dia_semana(7))
print(dia_semana(8))
    
"""
Exercício 3: calculadora simples
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao, que recebem dois números cada uma e retornam o resultado da operação indicada. 
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), que lê dois números e uma operação e exibe na tela o valor do 
resultado, ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações.

"""
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x, y):
    if y == 0:
        return  "Não pode dividir por zero >:("
    else:
        return x / y

def calculadora_cli():
    num1 =float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operadores = input('Digite o tipo de operação (+, -, *, /): ')
    if operadores == "+":
       resultado = adicao(num1, num2)
    elif operadores == "-":
       resultado = subtracao(num1, num2)
    elif operadores == "*":
       resultado = multiplicacao(num1, num2)
    elif operadores == "/":
       resultado = divisao(num1, num2)
    else:
        print("Operação Inválida")
     
    print('O resultado da operação é...', resultado)

calculadora_cli()
    
