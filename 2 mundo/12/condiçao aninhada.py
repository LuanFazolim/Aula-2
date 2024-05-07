t=int(input(':'))
if t <=3:
    print('Menor ou = a \033[34m 3\033[m ')

elif t >=3.1 and t <=6:
    print('Entre \033[34m 3\033[m  e \033[32m 6\033[m ')

elif t in (7, 8, 9):
    print('Entre \033[32m 6\033[m  e \033[35m 9\033[m ')

else:
    print('acima de \033[32m9 ')