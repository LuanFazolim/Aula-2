
maior=0
menor=0


for r in range(1,6):
    peso=float(input('Peso da \033[35m{}\033[m pessoa: '.format(r)))
    if r == 1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso < menor:
            menor=peso
print('O \033[35mmaior\033[m peso lido foi de \033[32m{}Kg\033[m'.format(maior))
print('O \033[31mmenor\033[m peso lido foi de \033[32m{}Kg\033[m'.format(menor))


