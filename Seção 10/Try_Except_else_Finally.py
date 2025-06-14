"""
Try / Except / Else / Finally

Dica de quando e onde tratar código

Toda entrada deve ser tratada

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# Exemplo mais complexo - Errado

def  dividir(a,b):
    return a/b

num1 = int(input('Digite um número: '))
try:
    num2 = int(input('Digite outro número'))
except ValueError:
    print('O valor deve ser numérico')

try:
    print(dividir(num1,num2))
except NameError:
    print('Valor incorreto')

"""

# Exemplo mais complexo - Correto

def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        # Metodo de tratatamento universal
        return f'Valor incorreto: {err}'

num1 = input('Num1: ')
num2 = input('Num2: ')

