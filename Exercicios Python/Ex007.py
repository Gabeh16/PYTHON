salario = float(input(print('Qual é o salário do funcionário? R$ ')))
aumento = (salario / 100) * 15
valorf = salario + aumento

print('Um funcionário  que ganhava R${:.2f}, com 15% de desconto, passa a receber R${:.2f}'.format(salario, valorf))