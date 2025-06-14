"""
Faça um programa que tenha uma função que recebe uma lista de inteiros e retorne o maior valor
"""
def maior(inteiros: int) -> int:
    return max(inteiros)


if __name__ == '__main__':
    lista: list[int] = [2,3,4,5,6,7,8,9,10]
    print(f'O maior valor na lista {lista} eh {maior(lista)}')