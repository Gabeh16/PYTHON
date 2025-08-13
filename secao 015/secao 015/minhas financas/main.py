from utilitarios import(
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total
)

# Categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_renda = cadastrar_categoria('Renda fixa')
categoria_viagens = cadastrar_categoria('Viagens')

# Transações

cadastrar_transacao(
    descricao='Salário 23/Abr',
    valor= 1500.0,
    categoria= categoria_receitas
)
cadastrar_transacao(
    descricao='Mesada',
    valor= 1200,
    categoria= categoria_receitas
)

cadastrar_transacao(
    descricao='Bico',
    valor = 300,
    categoria = categoria_receitas
)
cadastrar_transacao(
    descricao='shopping',
    valor = -130,
    categoria= categoria_viagens
)

total = saldo_total()

print(f'Saldo Total: {total}')

