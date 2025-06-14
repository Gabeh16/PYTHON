"""
Try/Except -> fazer o tratamento de erros


# Exeplo1 - Erro genérico

try:
    geek()
except:
    print('Deu algum problema ')

# Tente executar a função geek, se não achar
# Imprima uma mensagem de erro!

OBS: tratar erros de forma genérica não é bom
a melhor é tratar de forma espesifica.

# Exemplo 2 - Erro especifico
try:
    len(5)
except TypeError:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Exemplo 3 - Erro especifico com detelhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez

try:
    geek()
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")
except:
    print('Deu um erro diferente')
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
dic = {'nome':'Geek'}

print(pega_valor(dic,8))

