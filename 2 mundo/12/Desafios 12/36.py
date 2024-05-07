c=int(input('Valor da casa:'))
s=int(input('Salario R$:'))
a=int(input('Em quantos anos vc vai pagar:'))

m=c/(12*a)

d=30/100*s

s1=s-d

if s1>=m:
    print('Voce pagara \033[32m{:.2f} R$\033[m por \033[33mmes\033[m!!'.format(m))

else:
    print('\033[31mInfelizmente\033[m voce nao podera comprar!!')
