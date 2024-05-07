from datetime import date

n=int(input('Seu ano de nacimento: '))
a=(date.today().year)
i=a-n


print('\033[37m{} anos\033[m'.format(i))



print()
if i <=9:
    print('\033[33mMIRIM\033[m')


elif i >9 and i <=14:
    print('\033[31mINFANTIL\033[m')


elif i >14 and i <=19:
    print('\033[32mJUNIOR\033[m')


elif i >19 and i <=20:
    print('\033[34mSENIOR\033[m')


elif i > 20:
    print('\033[35mMASTER\033[m')