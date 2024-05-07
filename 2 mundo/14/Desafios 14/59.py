n1=float(input('Digite o \033[1;34m1\033[m valor: '))
n2=float(input('Digite o \033[1;35m2\033[m valor: '))
print(40 * '\033[37m=-\033[m')
print()

sn=0
#===================================================================

es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
    
    Escolha uma opçao acima: ''').strip())
print()

if es > 5 or es == 0:

    print(40 * '\033[37m=-\033[m')

    print()
    print('\033[31mOPS!!... numero invalido!\033[m')

    print(40 * '\033[37m=-\033[m')
    print()

    es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m

    Tente denovo!: ''').strip())
    print()






if es == 5:
    print('Voce deseja sair?')
    yn = str(input('[\033[1;32mY\033[m/\033[1;31mN\033[m]: ')).upper()[0]
    if yn == 'Y':
        es = 5

    elif yn == 'N':
        print()
        print(40 * '\033[37m=-\033[m')

        es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m

                Escolha uma opçao acima: ''').strip())
        print()

while not es  == 5:

    while es in (1,2,3,4):


        # ===================================================================
        # somar
        if es == 1:
            soma1=n1+n2
            print("A soma = \033[36m{}\033[m".format(soma1))
            print()
            print(40 * '\033[37m=-\033[m')


            es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
        
        Escolha uma opçao acima: ''').strip())
            print()

        #===================================================================

                #multiplicar
        if es == 2:
            mul=n1*n2
            print('A multiplicaçao = \033[36m{}\033[m '.format(mul))
            print()
            print(40 * '\033[37m=-\033[m')


            es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
        
        Escolha uma opçao acima: ''').strip())
            print()





        # ===================================================================
                #Maior
        if es == 3 and n1>n2:
             print('O \033[34m{}\033[m e maior que \033[31m{}\033[m'.format(n1,n2))
             print()
             print(40 * '\033[37m=-\033[m')
             es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
        
        Escolha uma opçao acima: ''').strip())
        print()




        if es == 3 and n2>n1:
            print('O \033[34m{}\033[m e maior que \033[31m{}\033[m'.format(n2, n1))
            print()
            print(40*'\033[37m=-\033[m')



            es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
        
        Escolha uma opçao acima: ''').strip())
            print()




        elif es == 3 and n1==n2:
            print('Os dois numeros sao \033[33mIguais!!\033[m')
            print()
            print(40 * '\033[37m=-\033[m')

            es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
        
        Escolha uma opçao acima: ''').strip())
            print()

        # ===================================================================
            # novos numeros
        if es == 4:
            print(40 * '\033[37m=-\033[m')
            n1 = float(input('Digite o 1 valor: '))
            n2 = float(input('Digite o 2 valor: '))
            print()
            print('Agora o \033[1;34m1 =\033[36m {}\033[m e o \033[1;35m2 =\033[36m {}\033[m'.format(n1,n2))

            print(40 * '\033[37m=-\033[m')
            print()



            es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m
    
    Escolha uma opçao acima: ''').strip())
            print()

        if es > 5 or es == 0:
            print(40 * '\033[37m=-\033[m')

            print()
            print('\033[31mOPS!!... numero invalido!\033[m')

            print(40 * '\033[37m=-\033[m')
            print()

            es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m

            Tente denovo!: ''').strip())
            print()

















        if es == 5:
            print('Voce deseja sair?')
            yn = str(input('[\033[1;32mY\033[m/\033[1;31mN\033[m]: ')).upper()[0]
            if yn == 'Y':
                es = 5

            elif yn == 'N':
                print()
                print(40 * '\033[37m=-\033[m')

                es = int(input('''[ 1 ] \033[33mSomar\033[m
[ 2 ] \033[34mMultiplicar\033[m
[ 3 ] \033[32mMaior\033[m
[ 4 ] \033[35mNovos numeros\033[m
[ 5 ] \033[31mSair do Programa\033[m

                        Escolha uma opçao acima: ''').strip())
                print()





































