# Exercício 10 (desafio)
# Você recebeu uma matriz de produtos, no mesmo formato usado no projeto de fundo
# ( [nome, preco, estoque] ):

# NOME, PRECO, ESTOQUE = 0, 1, 2
# produtos = [
# ["Caderno", 12.50, 5],
# ["Caneta", 2.30, 100],
# ["Mochila", 89.90, 3],
# ["Estojo", 15.00, 8],
# ]

# Use list comprehension para criar uma lista apenas com os nomes dos produtos que têm
# estoque menor que 10. 

NOME, PRECO, ESTOQUE = 0, 1, 2
produtos = [
    ["Caderno", 12.50, 5],
    ["Caneta", 2.30, 100],
    ["Mochila", 89.90, 3],
    ["Estojo", 15.00, 8],
]
nomes = [produto[NOME] for produto in produtos if produto[ESTOQUE] < 10]
print(nomes)
