from random import choice
from time import sleep

uad=[1,2,3,4,5,6,7,8,9,10]
print(15*'=-')
print('VAMOS JOGAR PAR OU IMPAR')
print(15*'=-')
#========================================================================================================
c=0
while True:
    poi=str(input('\033[1;35mPAR\033[m ou \033[1;36mIMPAR\033[m: ')).strip().lower()[0]
    while not poi in 'i p':
        print('\033[31mISSO NAO E UMA RESPOSTA VALIDA!!\033[m')
        poi = str(input('Tente outra vez...\033[1;35mPAR\033[m ou \033[1;36mIMPAR\033[m: ')).strip().lower()[0]


    num=int(input('Seu numero: '))
    comp=choice(uad)
    soma=num+comp



    if poi in 'p':
        print('\033[33mVoce\033[m e \033[35mPAR\033[m')
    if poi in 'i':
        print('\033[33mVoce\033[m e \033[36mIMPAR\033[m')



    print(10*'--')
    print('Par..',end='')
    sleep(0.4)
    print(' ou ',end='')
    sleep(0.4)
    print('..Impar!!')
    print(30*'--')





    if poi in 'i' and soma%2 == 0:

        print(f'Eu coloquei {comp} e voce {num}, somado da {soma} que e um numero \033[1;35mPAR\033[m')
        print(30 * '--')
        print('Entao \033[1;31mVoce perdeu!!\033[m',end=' ')
        break
    elif poi in 'p' and soma % 2 != 0:

        print(f'Eu coloquei {comp} e voce {num}, somado da {soma} que e um numero \033[1;36mIMPAR\033[m')
        print(30 * '--')
        print('Entao \033[1;31mVoce perdeu!!\033[m', end=' ')
        break



    if poi in 'p' and soma % 2 == 0 :

        print(f'Eu coloquei {comp} e voce {num}, somado da {soma} que e um numero \033[1;35mPAR\033[m')
        print(30 * '--')
        print('Entao voce \033[34mGanhou!!!\033[m')
        print(60 * '==')
        c+=1
    elif poi in 'i' and soma % 2 != 0:

        print(f'Eu coloquei {comp} e voce {num}, somado da {soma} que e um numero \033[1;36mIMPAR\033[m')
        print(30 * '--')
        print('Entao voce \033[34mGanhou!!!\033[m')
        print(60 * '--')
        c += 1








if c == 1:
    print(f'Voce so me venceu {c} vez!')
elif c > 1:
    print(f'Pelo menos me venceu {c} vezes')
elif c == 0:
    print(f'Voce nao me venceu nenhuma vez')

