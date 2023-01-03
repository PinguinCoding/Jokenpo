import random

print('Vamos jogar jokenpô! Faça sua jogada!')
jogadac = random.randint(1, 3)
rejogar = ''

while rejogar != 'NÃO':
    # Jogada do usuário
    jogadau = str(input('Digite "Pedra", "Papel" ou "Tesoura": ')).strip().upper()
    # Jogada do computador
    if jogadac == 1:
        jogadac = 'TESOURA'
    elif jogadac == 2:
        jogadac = 'PEDRA'
    else:
        jogadac = 'PAPEL'
   # Resultados
    if jogadau == jogadac:
        print(jogadac)
        print('Empatamos!')
        rejogar = str(input(('Quer jogar de novo? '))).strip().upper()
    elif jogadau == 'TESOURA' and jogadac == 'PEDRA':
        print(jogadac)
        print('Eu ganhei!')
        rejogar = 'NÃO'
    elif jogadau == 'TESOURA' and jogadac == 'PAPEL':
        print(jogadac)
        print('Você ganhou!')
        rejogar = 'NÃO'
    elif jogadau == 'PEDRA' and jogadac == 'PAPEL':
        print(jogadac)
        print('Eu ganhei!')
        rejogar = 'NÃO'
    elif jogadau == 'PEDRA' and jogadac == 'TESOURA':
        print(jogadac)
        print('Você ganhou!')
        rejogar = 'NÃO'
    elif jogadau == 'PAPEL' and jogadac == 'TESOURA':
        print(jogadac)
        print('Eu ganhei!')
        rejogar = 'NÃO'
    elif jogadau == 'PAPEL' and jogadac == 'PEDRA':
        print(jogadac)
        print('Você ganhou!')
        rejogar = 'NÃO'