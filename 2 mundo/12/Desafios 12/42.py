n1=float(input('Reta 1: '))
n2=float(input('Reta 2: '))
n3=float(input('Reta 3: '))

r1=n1+n2
r2=n1+n3
r3=n2+n3

if r1 >=n3 and r2 >n2 and r3>n1:
    print('E \033[32mpossivel\033[m fazer um triangulo!!')
    if n1 == n2 == n3:
        print('O triangulo e \033[33mEQUILATERO\033[m')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('O triangulo e \033[34mISOCELES\033[m')
    else :
        print('O triangulo e \033[35mESCALENO\033[m')
else:
   print('\033[31mNao\033[m e possivel formar um triangulo ')



