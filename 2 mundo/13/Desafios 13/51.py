p=int(input('Primeiro termo: '))
r=int(input('Razao: '))
for c in range(p,10*r,r):
    print('{} '.format(c),end='==> ')
print('FIM!')