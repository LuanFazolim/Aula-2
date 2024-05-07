print('Os numeros \033[34mpares\033[m de \033[32m1\033[m a \033[32m50\033[m sao:')

for p in range(2,50,2):
    print('\033[32m{}'.format(p))