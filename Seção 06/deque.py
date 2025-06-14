"""
Módulo Collections - Deque

Podemos dizer que é uma lista de alta performance

"""

from collections import deque

# Criando Deques

deq = deque('geek')

print(deq)


# Adicionando elementos no deque

deq.append('y')# Add no final
print(deq)

deq.appendleft('y')# Add no começo
print(deq)

# Remover elementos

deq.pop() # Remove e retorna o ultimo elemento
print(deq)

deq.popleft() # Remove e retorna o ultimo elemento
print(deq)