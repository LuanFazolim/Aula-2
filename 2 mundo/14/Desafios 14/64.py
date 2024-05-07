n=int(input('Digite um numero [999 para]: '))
c=0
s=0
while not n == 999:
    print('\033[1;31mNAO!!\033[m')
    n = int(input('Tente denovo [999 para]: '))
    c+=1
    s+=n


print()
s-=999
if s == -999:
    s+=999
print('Voce errou {} vezes\nE a soma entre eles e {}'.format(c,s))


