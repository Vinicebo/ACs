import random

def main():
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)
# atributos do aventureiro e monstro
    Rodada = 1
    print("Rodada", Rodada)
    print("Aventureiro: vida", vida_aventureiro, "- Ataque - ", ataque_aventureiro, "- Defesa -", defesa_aventureiro)
    print("Monstro: vida", vida_monstro, "- Ataque -", ataque_monstro)
#calculo das rodadas
    while vida_aventureiro > 0 and vida_monstro > 0:
        Rodada = Rodada + 1
        print("Rodada", Rodada)
        print("Aventureiro: vida", vida_aventureiro, "- Ataque - ", ataque_aventureiro, "- Defesa -", defesa_aventureiro)
        print("Monstro: vida", vida_monstro, "- Ataque -",ataque_monstro)
#calculo de dano do aventureiro
        dano_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstro = vida_monstro - dano_aventureiro
#calculo de dano do monstro
        dano_monstro = random.randint(1, ataque_monstro) - defesa_aventureiro
        if dano_monstro >= 0:
            vida_aventureiro = (vida_aventureiro - dano_monstro)

#monstro morre
        if vida_monstro <= 0:
            print("O monstro morreu!!")
            break
#aventureiro morre
        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break

main()
