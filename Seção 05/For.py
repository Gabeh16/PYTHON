qtd = int(input(print("Quantos loops deve ter? ")))
soma = 0
nome = "Cleiton Gás"
#Pedindo dados para o usuário em laço
for n in range(1, qtd+1):
    num = int(input(print(f"Informe o {n}/{qtd} valor:")))
    soma = soma+num
print(f"A soma é {soma}")

#Imprimindo sem pular linha
for pedra in nome:
    print(pedra, end="")

#Laço dentro de outro laço
for _ in range(3):
    for num in range(1,11):
        print('\U0001F600' * num)