"""
Módulo Random e o que são módulos?

- Em python, módulos nada mais são que outros arquivos
python.

Módulo random -> Possui várias funções para geração
de números pseudo-aleatório.


# Duas formas de utilizar um módulo ou função deste

# Forma 1 - Importando todo módulo.

import random

# Ao realizar o import de todo o módulo, todas
# as funções, atributos, classes e propriedades
# que estiverem dentro do módulo ficarão disponíveis
# ficarão em memória.

print(random.random())

# OBS: Não confundir a função random() com o pacote random

from random import random

for i in range (10):
    print(random())

# Uniform

from random import uniform

for i in range(10):
    print(uniform(3,7))
"""
from random import choice

jogadas = ['PEDRA','PAPEL','TESOURA']

print(choice(jogadas))