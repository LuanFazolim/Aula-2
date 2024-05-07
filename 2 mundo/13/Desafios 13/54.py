from datetime import date

atual=date.today().year
maior=0
menor=0


for a in range(1,7):
    ano=int(input('Em que ano a {} pessoa naceu?: '.format(a)))
    co=atual-ano
    if co < 18:
        maior+=1
    else:
        menor+=1

print('Ao todo tivemos \033[34m{}\033[m pessoas \033[34mmaiores\033[m de idade\nE tambem tivemos \033[33m{} menores\033[m de idade'.format(maior,menor))
