print(20*'==')
print(12*' ','BANCO ITACU')
print(20*'==')

sn='s'

while sn =='s':
    valor = int(input('Que valor voce quer sacar \033[32mR$\033[m  '))
    co50 = 0
    co20 = 0
    co10 = 0
    co1 = 0


    while 50<=valor:
        valor-=50
        co50+=1

    while 20<=valor:
        valor-=20
        co20+=1

    while 10<=valor:
        valor-=10
        co10+=1

    while 1<=valor:
        valor-=1
        co1+=1

    if co50 >= 1:
        print(f'\033[1;34m{co50}x\033[m = notas de \033[1;35mR$50\033[m')
    if co20 >= 1:
        print(f'\033[1;34m{co20}x\033[m = notas de \033[1;33mR$20\033[m')
    if co10 >= 1:
        print(f'\033[1;34m{co10}x\033[m = notas de \033[1;36mR$10\033[m')
    if co1 >= 1:
        print(f'\033[1;34m{co1}x \033[m= moedas de \033[1;32mR$1\033[m')


    print(22*'-')
    sn = str(input('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().lower()[0]
    print(22 * '-')
    print()
    print(20 * '==')
    while not sn in 's n':
        print('\033[31mNao entendi\033[m')
        sn = str(input('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().lower()[0]
    if sn == 'n':
        break



print('Volte sempre ao BANCO ITACU! Tenha um bom dia')



