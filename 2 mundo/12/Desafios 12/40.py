n1=float(input('Nota \033[35m1\033[m: '))
n2=float(input('Nota \033[35m2\033[m: '))

ng=(n1+n2)/2


print('Sua media foi \033[32m{}\033[m'.format(ng))

print()


if ng < 5:
    print('\033[31mREPROVADO!!!\033[m')


elif ng >= 5 and ng <=6.9:
    print('\033[33mRECUPERAÇAO!!!\033[m')


elif ng > 7:
    print('\033[34mAPROVADO!!!\033[m')
