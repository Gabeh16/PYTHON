cont = 0
soma = 0

while True :
    i = int(input("digite num:"))
    if i < 0:
        break

    soma += i
    cont += 1

if cont > 0:
    media = soma / cont
    print(f"{media:.2f}")