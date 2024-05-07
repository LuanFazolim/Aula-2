


from random import randint


print('\033[35m-=-'*20)

print('\033[36mVou pensar em um numero...')

print('\033[35m-=-\033[m'*20)

computador= randint(0,10)

jogador=int(input('Em que numero pensei? '))

soma=0

if jogador == computador and soma == 0:
    print()
    print('\033[32mParabens!!\033[m')
    print('Voce acertou de \033[36mPrimeira!!\033[m'.format(soma))

while computador != jogador:
    if computador>jogador:
        print()
        print('\033[31m Mais! \033[m ')
        jogador=int(input('Tente denovo: '))
        soma+=1

    else:
        print()
        print('\033[31m Menos! \033[m ')
        jogador = int(input('Tente denovo: '))
        soma += 1

    if jogador ==computador and soma !=1:
        print()
        print('\033[32mParabens!!\033[m')
        print('Voce acertou! mas foi depois de \033[31m{} erros\033[m'.format(soma))

    elif jogador ==computador and soma ==1:
        print()
        print('\033[32mParabens!!\033[m')
        print('Voce acertou! mas foi depois de \033[31m{} erro\033[m'.format(soma))
print()
#=============================================================================================
# outro jeito
print(60*'==')
print()
from random import randint
print('\033[35m-=-'*20)
print('\033[36mVou pensar em um numero...')
print('\033[35m-=-\033[m'*20)
computador= randint(0,10)

acertou=False
palpite=0
while not acertou:
    jogador=int(input('Qual e seu palpite: '))
    palpite+=1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos...Tente mais uma vez. ')

print('Acertou com {} tentativas. Parabens!!'.format(palpite))


