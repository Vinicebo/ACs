ano = int(input("Digite um ano: "))
print(((ano % 100 == 0 and ano % 400 == 0) and ano % 4 == 0) or (ano % 4 == 0 and ano % 100 != 0))