"""
**kwargs

Poderiamos chamar este parâmetro de **xis mas
por convenção chamamos de **kwargs

-> O kwargs exige que utilizemos parâmetros
nomeados e transforma em um dicionário


# Exemplo

def cores_favoritas(a,b,c,**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita {pessoa.title()}")
cores_favoritas(1,2,3,marcos='azul',cleber='verde')

# Os parâmetros *args e *kwargs não são obrigratorios

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico'
    elif 'geek' in kwargs:
        return f'{kwargs['geek']} Geek!'
    return 'Não certeza de quem você é'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


# Nas funções podemos ter (ORDEM)

# Parâmetros obrigatórios
# Args
# Parâmetro defaul ('Não obrigatórios):
# Kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} e {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado ')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity',4,5,6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19,'Carla',9,4,3, java=False, python=True)

-Entenda por quê é importante manter a ordem dos parâmetros na declaração

 ->Função com ordem certa de parâmetros
def mostra_info(a,b,*args, instrutor = 'Geek',**kwargs):
    #return [a, b, args, instrutor, kwargs]

 ->Função com a ordem incorreta de parâmetros
def mostra_info(a,b,instrutor = 'Geek',*args ,**kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1,2,3,sobrenome= 'University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes= {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))
"""


def soma_multiplo_numerico(a,b,c):
    print(a+b+c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}

# Desempacotando sem *args
soma_multiplo_numerico(*lista)# O '*' Desempacota
soma_multiplo_numerico(*tupla)
soma_multiplo_numerico(*conjunto)

dicionario= dict(a=1, b=2,c=3)

soma_multiplo_numerico(*dicionario)

# O nome da chave de dicionario tem que ser igual ao do parâmetro da função
