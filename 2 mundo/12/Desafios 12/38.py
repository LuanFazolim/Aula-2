n1=float(input('N1: '))
n2=float(input('N2: '))

if n1 > n2:
    print('O numero \033[32m{}\033[m e \033[34mmaior!!\033[m'.format(n1))

elif n1 < n2:
    print('O numero \033[32m{}\033[m e \033[34mmaior!!\033[m'.format(n2))

elif n1 == n2:
    print('Os 2 numeros sao \033[33miguais!!\033[m')