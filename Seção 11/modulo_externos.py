"""
Modulos Externos

Utilizamos o gerenciador de pacotes Python chamado
Pip - Python Intaller Package


"""

from colored import Fore,Back,Style

print(Fore.red + 'Gabriel')
print(Fore.black + 'Costa')
print(Fore.white + 'Diares')

print(Fore.white + 'VAMOS COMEÇAR A PROGRAMAR' )
print(Fore.green + '=================================================================')
for i in range(0,11):
    v1 = i * 2
    print(f'{Fore.white} {v1}', end="")

print(Fore.green + '\n=================================================================')

print(Fore.green + '=================================================================')
for i in range(0,11):
    v2 = i / 2
    print(f'{Fore.white} {v2}', end="")

print(Fore.green + '\n=================================================================')