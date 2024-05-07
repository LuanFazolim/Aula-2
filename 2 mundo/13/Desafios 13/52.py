n=int(input('n: '))
tot=0

for p in range(1,n+1):
    if n % p ==0:
        print('\033[32m', end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print('{} '.format(p), end='')
print()
print('\033[mO numero {} e divisivel {} vezes'.format(n,tot))
if tot ==2:
    print('E por isso ele e \033[34mPRIMO\033[m')
else:
    print('Ele \033[31mNAO\033[m e primo')

