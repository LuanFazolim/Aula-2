print('-'*30)
print('   Sequencia de Fibonacci')
print('-'*30)
n=int(input('Quantos termos voce quer mostrar: '))
c=3
n1=0
n2=1
print('{} => {}'.format(n1,n2),end=' => ')
while c <= n:
    c+=1
    n3 = n1 + n2
    n1=n2
    n2=n3
    print('{}'.format(n3),end=' => ')

print('...')
