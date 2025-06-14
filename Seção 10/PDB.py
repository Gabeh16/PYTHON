"""
PDB


def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError,ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0 ))

"""
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace