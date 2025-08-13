"""
-> Manipulando data hora

Biblioteca DateTime

#print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

print(datetime.datetime.now())

#datetime.datetime(year,month,day,hour,minute,second,microsecond
print(repr(datetime.datetime.now()))

#Replace()

inicio = datetime.datetime.now()

print(inicio)


# Alterar o horario para 16 horas
inicio = inicio.replace(hour=16,minute=30,second=25)

-> Recebendo dados do usuario e convertendo

evento = datetime.datetime(2019,1,1,0)

print(type(evento))

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

print(nascimento)

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]),int([nascimento[0]))

print(type(nascimento))

print(nascimento)

"""

import datetime

evento = datetime.datetime.now()




print(evento.year())
print(evento.month())
print(evento.day())
print(evento.hour())
print(evento.minute())

print(dir(evento))