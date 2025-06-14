produto = float(input(print('Qual é o preço do produto? R$')))
desconto = (produto / 100) * 5
valor = produto - desconto
print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${valor}')

