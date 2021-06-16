numeros = list(range(1, 11))
numerosx10 = []

for numero in numeros:
    numerosx10.append(numero*10)

print(numerosx10)

for indice, numero in enumerate(numeros):
    numerosx10[indice] = numeros[indice] * 10

print(numeros)

print(numerosx10)
