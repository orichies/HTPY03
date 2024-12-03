# Exercício 5: Contar Números Pares
# Escreva um programa que receba 10 números inteiros e conte quantos deles são pares.

pares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        pares.append(numero)

print(f"Quantidade de números pares digitados: {pares}")