s=0
c=0
while True:
    n=int(input('Digite um numero (999 faz parar): '))

    if n == 999:
        break

    c+=1
    s+=n
print(f'A soma de {c} valores foi {s}!')