n=0
n1=n
m=0
p=0
yn='S'.upper()
d=s=c=0


while yn == 'S':
    n=float(input('Digite um valor: '))

    # media
    s += n
    c += 1

    if c == 1:
        m=p=n
    else:
        if n>m:
            m=n
        if n<p:
            p=n





    yn=str(input('Quer continuar?\n [\033[1;32mS\033[m/\033[1;31mN\033[m]:')).upper().strip()[0]
    print()





d=s/c
print('A media de todos os numeros e de {:.2f} \nO maior e {} e o menor {} '.format(d,m,p))