print('\033[34mIMC\033[m')

print('')

p = float(input('\033[7mPeso\033[m: '))

a = float(input('\033[7;36mAltura \033[m(*\033[35m.\033[m**): '))

e = a * a

f = p / e

print()

print('seu \033[34mIMC\033[m é de:\033[37m{:.2f}\033[m'.format(f))

print()

if f <= 18.5:
    print('\033[32mAbaixo do peso!')

elif f >= 18.5 and f <= 24.9:
    print('\033[34mPeso normal')

elif f >= 25 and f <= 29.9:
    print('\033[33mAcima do peso(sobrepeso)\033[m')

elif f >= 30 and f <= 34.9:
    print('\033[31mObesidade 1')

elif f >= 35 and f <= 39.9:
    print('\033[31mObesidade 2')

elif f >= 40:
    print('\033[31;40mObesidade 3!!\033[m')



# Menor do que 18,5 = abaixo do peso



# entre 18,5 e 24,9 = peso normal



# entre 25 e 29,9 = acima do peso (sobrepeso)



# entre 30 e 34,9 = obesidade 1



# entre 35 e 39,9 = obesidade 2



# maior do que 40 = obesidade 3