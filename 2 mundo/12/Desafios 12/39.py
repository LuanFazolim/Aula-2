from datetime import date

a=int(input('Seu ano de nascimento: '))
a2=(date.today().year)
a1=a2-a


if a1 < 18:
    print('\033[32mainda\033[m se alistara!!'),
    t=18-a1
    print('Falta \033[35m{} anos\033[m para se alistar '.format(t))


elif a1 == 18:
    print('\033[33mHora\033[m de se alistar !!!')



elif a1 > 18:
    print('\033[31mPassou\033[m o tempo!!!'),
    t2=a1-18
    print('Atrasado \033[35m{} anos\033[m do alistamento'.format(t2))
