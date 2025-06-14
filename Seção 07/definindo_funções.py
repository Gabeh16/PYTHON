"""
Definindo Funções

- Funções são pequenas partes de código que realizam
tarefas especificas:
- Pode ou não receber entradas de dados e retornar uma
saída de dados:
- Muito uteis para executar procedimentos similares
por repetidas vezes

OBS: Se você escrever uma função que realiza várias
tarefas dentro dela é bom fazer uma verificação para
que a função seja simplificada.


Já utilizamos várias funções
- print()
- max()
- min()
- count()
"""
# Exemplo de utilização de funções

#cores = ['verde', 'azul', 'verde', 'branco']

# utilizando a função integrada (Built-in) do Python

#print(cores)

#curso = "Programação em Python"

#print(curso )

#cores.append('Roxo')

#print(cores)

#curso.append('Mais dados')# Attribute Error
#print(curso)

#cores.clear()
#print(cores)

# Como definir funções

"""
Em python a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada):
    bloco_da_função
    
- nome da função -> sempre minusculo
- parametros de entrada -> Opcionais, onde tendo mais
de um, deve ser separado por virgula 
- bloco da funcao -> Onde o processamento da função
acontece pode ter ou não retorno da função 
"""
# Definindo a primeira função

# Definição
def diz_oi ():
    print('oi')

"""
OBS:

1 - Dentro de uma função podemos usar outras funções
2 - A função so pode executar uma única tarefa apenas diz 'oi'
3 - Essa função não recebe parametro-de-entrada
4 - Essa função não retorna nada 
"""
# utilizando funções

# Chamada de execução
diz_oi()

# Exemplo 2
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

#for n in range(4):
#   print(n)
#   cantar_parabens()

# Em python podemos criar variaveis do tipo função
# E executar essa função através da variável

canta = cantar_parabens
canta()