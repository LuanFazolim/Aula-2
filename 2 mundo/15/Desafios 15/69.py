print(20*'--')
print('         CADASTRE UMA PESSOA')
print(20*'--')
co18=0
masc=0
mu=0
co20=0
while True:
    idade=int(input('Sua idade: '))
    if idade>18:
        co18+=1

    # sexo
    sexo=str(input('Seu sexo [\033[34mM\033[m/\033[35mF\033[m]: ')).strip().lower()[0]
    if sexo in'm':
        masc+=1
    if sexo in 'f' and idade<20:
        mu+=1


    while not sexo in 'm f':
        print('\033[31mSEXO NAO RECONHECIDO!!\033[m')
        sexo = str(input('Tente novamente...Seu sexo [\033[34mM\033[m/\033[35mF\033[m]: ')).strip().lower()[0]
    #==========================================================================
    print(25*'-')
    sn=str(input('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().lower()[0]

    while not sn in 's n':
        print('\033[31mNao entendi\033[m')
        sn = str(input('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().lower()[0]
    if sn == 'n':
        break
    print()
    print(20 * '--')
    print('         CADASTRE OUTRA PESSOA')
    print(20 * '--')
print()

if co18 == 1:
    print(f'Tivemos apenas {co18} pessoa com mais de 18 anos ')
if co18 == 0:
    print('Nao tivemos pessoas com mais de 18 anos')
if co18 >1:
    print(f'Total de pessoas com mais de 18 anos: {co18}')


if masc == 1:
    print(f'Ao todo temos apenas {masc} homen cadastrados')
if masc == 0:
    print(f'Ao todo nao tivemos homens cadastrados')
if masc > 1:
    print(f'Ao todo tivemos {masc} homens cadastrados')




if mu == 1:
    print('E temos apenas 1 mulher com menos de 20 anos')
if mu == 0:
    print('E nao tem nenhuma mulher com menos de 20 anos')
if mu>1:
    print(f'E temos {mu} mulheres com menos de 20 anos')