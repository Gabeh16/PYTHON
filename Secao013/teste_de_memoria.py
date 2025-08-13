"""
Teste de memoria com generartors

-> Menor consumo de memoria

# TESTE

for n in fib_lista(100):
    print(n)



def fib_lista(max):
    nums = []
    a,b = 0,1
    while len(nums) < max:
        nums.append(b)
        a,b = b, a+b
    return nums

def fib_gen(max):
    a,b,contador = 0,1,0
    while contador <= max:
        a,b = b, a + b
        yield a
        contador = contador + 1

# TESTE 2
    for num in fib_gen(100000):
        print(num)
"""
