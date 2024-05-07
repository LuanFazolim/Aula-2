print('Ex \033[35m1\033[m')
print('So acaba quando voce digita um verbo que esta no \033[36mSingular\033[m')
print()
pal=input('Digite uma palavra: ')
l=len(pal)
aei=pal[l-2:l+1:].strip().lower()
re=pal[:l-2:].capitalize()

while not aei in 'ar er ir':
    print('\033[31mNao\033[m e um verbo no \033[36mSingular!!\033[m')
    print()
    pal=input('Tente novamente: ')
    l = len(pal)
    aei = pal[l - 2:l + 1:].strip().lower()
    re = pal[:l - 2:].capitalize()
print('\033[32mSim\033[m, isso e um verbo no \033[36mSingular!!\033[m')
print(re + ' \033[34m{}\033[m'.format(aei))


print()
print(130*'\033[31m=\033[m')
#============================================================================================
print()
print('Ex \033[35m2\033[m')
print()

n='S'
while n =='S':
    n1=float(input('Digite o 1 numero: '))
    print('                     +')
    n2=float(input('Digite o 2 numero: '))
    print('= \033[34m{}\033[m'.format(n1+n2))
    n=input('Deseja continuar [\033[32mS\033[m/\033[31mN\033[m]?: ').upper()
    print()


print()
print(130*'\033[31m=\033[m')
#============================================================================================
print()
print('Ex \033[35m3\033[m')
print('Ao digitar \033[34m0\033[m acaba')
print()

n=1
s=0
par = 0
impar = 0

while n != 0:
    n=int(input('Digite um valor: '))
    s+=1
    p=n%2

    if p == 0:
        par+=1
    else:
        impar+=1



print('Foram \033[35m{}\033[m numeros antes do \033[34m0\033[m'.format(s))
print('Tivemos \033[36m{}\033[m \033[34mPares\033[m'.format(par-1))
print('E \033[36m{}\033[m \033[34mImpares\033[m'.format(impar))