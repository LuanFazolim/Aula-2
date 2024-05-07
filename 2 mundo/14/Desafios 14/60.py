n=int(input('Digite um numero: '))
c=n
m=1
print('{}! = '.format(n),end='')
while c>0:


    if c == 1:
        print(c, end=' = ')
    else:
        print(c,end=' x ')

    m *= c
    c-=1

print('\033[34m{}'.format(m))






















