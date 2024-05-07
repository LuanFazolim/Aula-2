soma= 0
cont= 0

for c in range(1,7):
    num=int(input('Numero {}: '.format(c)))
    if num % 2==0:
        soma+=c
        cont+=1

print('Voce informou {} numeros, e as somas dos pares dao {}'.format(cont,soma))