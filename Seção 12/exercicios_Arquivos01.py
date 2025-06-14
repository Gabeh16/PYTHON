"""
Criar um programa para
"""

with open('arq.txt', 'a') as arquivo:
    while True:
        caractere: str = input("informe um caractere ou 0 para SAIR:")

        if caractere != '0':
            arquivo.write(f'{caractere}\n')
        else:
            break


with open('arq.txt','r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha)