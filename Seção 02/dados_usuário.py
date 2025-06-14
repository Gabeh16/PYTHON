"""
-Recebendo dados do usuário

input() -> Tudo que for recebido via input é string

nome = input(print("Qual o seu nome?"))

-Cast
Mudar um tipo de dado por outro 

{int(idade)}

-Formas de formatação
-> %s %(Var, Var)
-> print("A {0} tem {1} anos". format(nome, idade))
-> print(f"A {nome} tem {idade}")

Em python STRING é tudo que estiver entre aspas
"""
#Entrada de dados

#Abreviando
#nome = input(print('Qual o seu nome?'))

#Forma Antiga
#print("Seja bem vindo(a) %s" % nome)

#Forma Nova
#print("Seja bem vindo(a) {0}".format(nome))

#Forma mais moderna
#print(f"Seja bem vindo(a) {nome}")


#idade = int(input(print("Qual a sua idade? ")))

#Processamento

#Saída

#Modo novo
#print("A %s tem %s anos" % (nome, idade))
#Modo Moderno
#print("A(O) {0} tem {1} anos".format(nome,idade))

#Modo mais moderno
#print(f"O{nome} tem {idade} anos")

"""
#int(idade) => cast

Cast seria a conversão de um tipo de dado
em outro tipo

EXEMPLO
"""

#print(f"Logo{nome} nasceu em {2024 - (idade)}")

nome = input(print("Qual o seu nome?"))

print(f"Olá {nome} seja bem vindo(a)")

idade = int(input(print("Quantos anos você tem?")))

print(f"O {nome} tem {idade} anos que legal!")

telefone = int(input(print("Qual o seu número  de telefone?")))

print(f"Então seu número  de telefone é {telefone}")
print(f"Então {nome} nasceu em {2024 - idade} tem {idade} anos e seu número é {telefone}")