# Exercício 3: Maior de Três Números
# Escreva um programa que receba três números inteiros e determine qual deles é o maior.

numeros = []

for i in range(3):
    numeros.append(int(input(" digite um numero: ")))

numeros.sort()
print(f"o maior número é {numeros[len(numeros)-1]} e o menor número é: {numeros[0]}")    
