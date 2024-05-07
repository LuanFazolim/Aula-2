
m=''
f=''
while m != 'm' and f !='f':
    m=f=input('[\033[1;34mM\033[m/\033[1;35mF\033[m]: ').lower()[0]

    if m != 'm' and f != 'f':
        print('\033[1;31mISSO NAO E UMA RESPOSTA VALIDA!!\033[m')

    if m == 'm':
        print('\033[34mHomem\033[m')
    elif f == 'f':
        print('\033[35mMulher\033[m')


#================================================================================
#outro jeito

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('\033[1;31mISSO NAO E UMA RESPOSTA VALIDA!!\033[m')
    sexo = str(input('Informe seu sexo!! [M/F]: ')).strip().upper()[0]

print('sexo {} registrado com sucesso'.format(sexo))

