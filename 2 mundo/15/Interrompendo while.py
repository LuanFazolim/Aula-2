yn=str(input('[S/N]: ')).upper().strip()[0]
s='S'
while s == 'S':
    print('Continuar?')
    yn = str(input('[S/N]: ')).upper().strip()[0]
    if yn == 'N':
        print()
        print('Tchau!!')
        break

