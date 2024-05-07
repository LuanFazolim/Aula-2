print(19*'-=')
print('            LOJA DO LUEN')
print(19*'-=')
#=========================================================================================
total=0
mqm=0
c=0
men=0
n=''

while True:
    nome=str(input('Nome do produto: '))

    #preço
    preco=float(input('Preço \033[32mR$ \033[m'))
    total+=preco
    c+=1

    if preco > 1000:
        mqm+=1


    if c == 1:
        men=preco
        n=nome
    else:
        if men>preco:
            men=preco
            n=nome
        else:
            men=men





    #====================================================================================



    #SIM ou NAO
    sn = str(input('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().lower()[0]
    while not sn in 's n':
        print('\033[31mNao entendi\033[m')
        sn = str(input('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().lower()[0]
    if sn == 'n':
        break
    print(30*'-')
    #=======================================================================================
print(f'O preço total foi de \033[32mR${total}\033[m')
print(f'Temos \033[34m{mqm}\033[m produtos custando mais de \033[32mR$1000\033[m')
print(f'O produto mais barato foi \033[35m{n}\033[m que custa \033[32mR${men}')