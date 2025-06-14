"""
With

Funciona como um processo de abertura e fechamento rápido de arquivos
muito mais eficiente do que só usar o open()

"""
# O 'as' é usado para dar um nome ao 'texto.text'

with open('texto.text') as arquivo:
    print(arquivo.read())

# É impossivel  executar de novo, poís o with já fechou.


