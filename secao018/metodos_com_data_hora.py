"""
Metodos data hora


# Com now é possivel explicar fusos horarios
agora = datetime.datetime.now()
print(agora)
print(type(agora))

# Com today não é possivel usar fusos
hoje =datetime.datetime.today()
print(hoje)

# Mudancas ocorrendo durante a noite no sistema

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days = 1)),datetime.time())

print(manutencao)
print(type(manutencao))


manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days = 1)),datetime.time())

print(manutencao.weekday())
"""

import datetime

aniversario = input('Qual sua data de aniversario?')

aniversario = aniversario.split('/')




