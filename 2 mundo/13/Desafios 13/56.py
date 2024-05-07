
soma=0
maior=0
nomevelho=''
cont=0


for fo in range(1,5):
    print('-----{}ª PESSOA -----'.format(fo))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/f]: ')).strip()

    #Media
    soma+=idade
    #=================================================================================

     #velho
    if fo == 1 and sexo in 'Mm':
        maior=idade
        nomevelho=nome

    if sexo in 'Mm' and idade>maior:
        maior=idade
        nomevelho=nome


    #==================================================================================

    #mulheres

    if sexo in 'Ff' and idade < 20:
        cont+=1



#media
media=soma/4
print('A \033[35mmedia\033[m de idade do grupo e de \033[32m{}\033[m anos'.format(media))
#=================================================================================
print()
#velho
print('O homen mais \033[34mvelho\033[m tem \033[32m{}\033[m anos e se chama \033[36m{}\033[m'.format(maior,nomevelho))

#mulher
print()
if cont <=1:
    print('Ao todo temos \033[32m{}\033[m mulher com menos de \033[33m20 anos'.format(cont))

else:
    print('Ao todo tem \033[32m{}\033[m mulheres com menos de \033[33m20 anos'.format(cont))