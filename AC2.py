"""
Exercício 1: revisite a AC1
Desenvolva duas funções em Python:

eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0, supondo as raízes sempre reais;
bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
"""
def equacao_de_seguno_grau(a,b,c):
        #primeiro ele resolverá o delta
    d = (b**2) - (4*a*c)
        
    #deepois as duas soluuções
    raiz1 = (-b + (d)**0.5) / (2*a)

    raiz2 = (-b - (d)**0.5) / (2*a)

    return (raiz1, raiz2)

#a função print foi escrita apenaas com o intouito de teste
print(equacao_de_seguno_grau(1, -6, 8))

"""
"""
def bissexto(ano):
  
   #isto anlisará se o ano é divisível por 100, 400 e 4 ou 100 e 4  
   return ano % 100 == 0 and ano % 400 == 0 and ano % 4 == 0 or ano % 4 == 0 and ano % 100 != 0

#a função print foi escrita apenaas com o intouito de teste
print(bissexto(95))

"""
Exercício 2: salário
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe dois parâmetros posicionais reais,
valor_hora e num_horas, que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente. 
Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275. 
A função retorna o salário líquido de um funcionário, calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado
"""
def calcula_salario(valor_hora, num_de_horas):
    #valor do imposto fixo
    irfp = 0.275
    return (round(valor_hora * num_de_horas)*irfp)

#a função print foi escrita apenaas com o intouito de teste
print(calcula_salario(1000, 5))
