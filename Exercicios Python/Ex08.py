diaria = float(input(print('Quanros dias alugados? ')))
km = float(input(print('Quantos Km rodados')))

dia = diaria * 60
rodagem = float(km * 0.15)
total = dia + rodagem
print(f'O total a pagar é {total}')
