# Exercício 8
# Dada a lista numeros = [3, 8, 15, 22, 7, 40, 11] , use list comprehension para criar uma
# nova lista contendo apenas os números pares.

numeros = [3, 8, 15, 22, 7, 40, 11]
pares = [n for n in numeros if n % 2 == 0]
print(pares)