"""
Modos de arquivos

-> R = Default modo padrão
-> W = Modo de escrita para escrevermos nos arquivos
-> X = Abre somente arquivos que estiverem fechados caso contrário aparece erro
-> A = Abre para escrita adicionando conteúdo para o final do arquivo semore ao final
-> + = Abre para modo de atualização


"""

with open('novo.txt', 'a') as arquivo:
    arquivo.write('Novos modelos \n')
    arquivo.write('Nova forma')

with open('novo.txt','x') as arq:
    arquivo.write('Mais Avaliados')
    arquivo.write('Menos Avaliados')