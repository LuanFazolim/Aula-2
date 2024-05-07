pe=input('Digite algo: ')

sp1=pe.split()
ju1=''.join(sp1)

i = ''

for re in range(len(ju1)-1,-1,-1):
    i+=ju1[re]
print('O \033[33minverso\033[m de \033[36m{}\033[m e \033[35m{}\033[m'.format(ju1,i))
if i == ju1:
    print('Temos um \033[34mPALIDROMO!!\033[m.')


else:
    print('\033[31mNAO\033[m temos um palidromo')







