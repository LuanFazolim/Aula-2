n=int(input('n: '))
print('''Escolha uma das bases para conversao:
[ 1 ] Converter para \033[35mBINARIO \033[m
[ 2 ] Converter para  \033[34mOCTAL \033[m
[ 3 ] Converter para  \033[33mHEXADECIMAL \033[m''')
o=int(input('Sua opçao?: '))

#1
if o == 1:
    print ('\033[32m{} \033[m Convertido para  \033[35mBINARIO \033[m fica  \033[35m{} \033[m'.format(n,bin(n)))


#2
elif o == 2:
    print('\033[32m{} \033[m Convertido para  \033[34mOCTAL \033[m fica  \033[34m{} \033[m'.format(n, oct(n)))



#3
elif o == 3:
    print('\033[32m{} \033[m Convertido para  \033[33mHEXADECIMAL \033[m fica  \033[33m{} \033[m'.format(n, hex(n)))



#invalida
else:
    print('Essa opçao e \033[31mINVALIDO!! \033[m')
