from agenda import Agenda

"""
 2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:

 a) armazenar_contato(contato: Contato);
 b) remover_contato(contato: Contato);
 c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
 d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
 e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice

"""

lista_contatos = []

def armazenar_contato(contato):
    novo_contato = Agenda(contato)

    lista_contatos.append(novo_contato)

    return novo_contato

def remover_contato(contato):
    remove_ctt = Agenda(contato)

    lista_contatos.pop(contato)

    return remove_ctt

def buscar_contato(contato):
    busca_ctt = Agenda(contato)
    
    lista_contatos.index(contato)

    return busca_ctt

def imprimir_agenda():
    return f'Dados nome: {Agenda.nome}, sobrenome: {Agenda.sobrenome}, idade: {Agenda.idade} email: {Agenda.email}'

def imprimir_contato():
    pass

