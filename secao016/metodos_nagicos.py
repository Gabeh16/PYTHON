"""
POO - Metodos Mágicos

Todos os metodos que usam DUNDER

# REPR
    def __repr__(self):
        return self.titulo, self.autor
"""

class Livro:

    def __init__(self,titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo, self.autor

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto foi deletado!')

livro = Livro('Python rocks', 'Cleiton',230)
livro2 = Livro('IA em Python ','tom hawks',330)

print(livro)
print(livro2)

print(len(livro))
print(len(livro2))
