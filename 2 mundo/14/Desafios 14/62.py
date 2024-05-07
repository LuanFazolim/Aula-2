print('\033[34m==== GERADOR DE PA ====\033[m')
print('-='*50)

p=int(input('Primeiro termo: '))
r=int(input('Razao: '))

p1=p
c=1
mais=10
total=0
while  mais != 0:
    total=total+mais
    while c <= total:
        print('{}'.format(p),end=' => ')
        c+=1
        p += r
    print('...')


    mais=int(input('\nQuer mostrar mais quantos: '))
print()
print('Ate mais!!')



