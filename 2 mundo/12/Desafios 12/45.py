print('\033[34m                                                                       Jokenpoo!!\033[m')
print(52*'\033[35m-=-\033[m')
print()
print('Vamos brincar de \033[34mJokenpoo!!\033[m',end='')

from random import choice
from time import sleep

a1=('pedra','papel','tesoura')
a=choice(a1)

print('\033[37m.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.\033[m')
sleep(0.5)

print('Escolha entre \033[40mPedra\033[m , \033[36mPapel \033[m e \033[31mTesoura\033[m ... ')
print()

ppt=input('\033[35m>>')
print('')
print('\033[37mPedra!...',end='')
sleep(0.5)
print('Papel!!...',end='')
sleep(0.5)
print('Tesoura!!!\033[m')
sleep(0.5)

if a == 'pedra':
    print('                                                                      \033[36mpedra \033[mX \033[32m{}\033[m'.format(ppt))


elif a == 'papel':
    print('                                                                      \033[36mpapel \033[mX \033[32m{}\033[m'.format(ppt))


if a == 'tesoura':
    print('                                                                      \033[36mtesoura \033[mX \033[32m{}\033[m'.format(ppt))

print()




print(39*'\033[35m=~~=\033[m')
print()

if a == 'pedra' and ppt == 'papel':
    print('\033[35mParabens!!\033[m, voce me venceu!')

elif a == 'tesoura' and ppt == 'pedra':
    print('\033[35mParabens!!\033[m, voce me venceu!')

elif a == 'papel' and ppt == 'tesoura':
    print('\033[35mParabens!!\033[m, voce me venceu!')

#win cpu

if ppt == 'pedra' and a == 'papel':
    print('Voce \033[31mperdeu!!\033[m')

elif ppt == 'tesoura' and a == 'pedra':
    print('Voce \033[31mperdeu!!\033[m')

elif ppt == 'papel' and a == 'tesoura':
    print('Voce \033[31mperdeu!!\033[m')

if ppt==a:
    print('Putz.',end='')
    print('.',end='')
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('\033[33mEmpatamos!!')