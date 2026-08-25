# Exercício 9
# Dada a lista numeros = [3, 8, 15, 22, 7] , use list comprehension com expressão
# condicional ( if / else dentro da expressão) para criar uma lista com a string "par" ou
# "ímpar" correspondente a cada número, na mesma ordem

numeros = [3, 8, 15, 22, 7]
print(numeros)
resultado = ['par' if numero % 2 == 0 else 'ímpar' for numero in numeros]
print(resultado)