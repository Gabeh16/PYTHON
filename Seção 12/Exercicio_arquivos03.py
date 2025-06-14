"""
3.Faça um programaque receba do usuário o nome de um arquivo texto e mostre
na tela quantas linhas este arquivo possui.
"""

arquivo: str = input("informe o nome de arquivo para abrir: ")

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()

print(f'Existem(m) {len(linhas)}linha(s) no arquivo. ')


