pr=float(input('Valor do produto: '))
cp1=str(input('Como deseja pagar \033[33mA vista\033[m ou \033[36mParcelado\033[m: '))

cp=cp1.lower()


#a vista

if cp == 'a vista' or cp == 'avista':
    av1=str(input('\033[34mDinheiro / Cheque\033[m ou \033[35mCartao\033[m?: '))
    av=av1.lower()

    if av == 'dinheiro' or av == 'cheque':
        p=10/100*pr
        d=pr-p
        print('No \033[34mDinheiro / Cheque\033[m, o produto sai por \033[32m{} R$'.format(d))
    elif av == 'cartao':
        p2 = 5 / 100 * pr
        d2 = pr - p2
        print('No \033[35mCartao\033[m, o produto sai por \033[32m{} R$'.format(d2))

#parcela

if cp == 'parcelado' or 'parcela' or 'parcelas':
        par=str(input('Em \033[34m2x\033[m ou \033[35m3x ou mais\033[m?: '))
        par1=par.lower()
        if par1 == '2x':
            print("Em \033[34m2x\033[m no cartao, o preço fica o mesmo'\033[32m{} R$\033[34m".format(pr))
        elif par1 =='3x' or 'mais':
            pa1=int(input('Em quantas parcelas?: '))
            p3 = 20 / 100 * pr
            d3 = pr + p3
            pa=d3/pa1
            print()

            print('Voce pagara \033[32mR${}\033[m durante o periodo de \033[35m{}\033[m meses.'.format(pa,pa1))
            print()


            print('Em \033[35m{}x\033[m no cartao, o preço ao todo fica. \033[32mR${}\033[m'.format(pa1,d3))




