"""
Saindo de loops com Break

Utilizamos o break para sair de loops de maneira
projetada
"""
#Exemplo 1
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do LOOP")

#Exemplo 2
while True:
    comando = input("Digite sair para sair ")
    if comando == "sair":
        break
    elif comando != "sair":
        print("Você é burro!")
