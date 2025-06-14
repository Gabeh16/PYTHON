"""
Faça um programa que receba uma data no formato String exemplo "01/01/1001"
e imprima ela por extenso como 1 de janeiro de 2024"
"""
def data_por_extenso(data: str) -> None:
    d = data.split('/')

    dia = int(d[0])
    mes = int(d[1])
    ano = int(d[2])

    if mes == 1:
        mes_str = 'janeiro'
    elif mes == 2:
        mes_str = 'fevereiro'
    elif mes == 3:
        mes_str = 'março'
    elif mes == 4:
        mes_str = 'abril'
    elif mes == 5:
        mes_str = 'maio'
    elif mes == 6:
        mes_str = 'junho'
    elif mes == 7:
        mes_str = 'julho'
    elif mes == 8:
        mes_str = 'agosto'
    elif mes == 9:
        mes_str = 'setembro'
    elif mes == 10:
        mes_str = 'outubro'
    elif mes == 11:
        mes_str = 'novembro'
    elif mes == 12:
        mes_str = 'dezembro'
    else:
        mes_str = 'desconhecido'

    print(f'{dia} de {mes_str} de {ano}')
if __name__ == '__main__':
    data_por_extenso('01/01/2024')
