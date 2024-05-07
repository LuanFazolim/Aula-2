#normal
print('\033[32mnormal\033[m')
for c in range(3,):
    s=input('como estas: ')

print('\033[33mObrigado!\033[m')

print()
#------------------------------------------------------------------------------------------
print(67*'=-')
print('\033[35mPulo\033[m')

print()
#pulo
for t in range(0,3):
    r=input('Esta bem?: ')
    k=input('voce gosta de cenoura?:')

print('\033[33mObrigado!\033[m')



print()

#-----------------------------------------------------------------------------------------------------------------
print(67*'=-')
print("\033[33mPULO VARIAVEIS\033[m")
print()
for de in range(6,0,-1):
    print(de)



print()

#-----------------------------------------------------------------------------------------------------------------
print(67*'=-')
print("Com '\033[34mif\033[m'")
print()

for b in range(0,3):
    bem=str(input('Voce esta bem?: '))
    bem.lower()
    if b == 'sim' or 's':
        print('Que \033[32mbom!!\033[m')
    else:
        print('Isso e \033[31mruim!\033[m')

