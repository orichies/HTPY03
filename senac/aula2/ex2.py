# Exercício 2: Soma de Números Positivos
# Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. Exiba a soma de todos os números positivos digitados.

# Inicializa a soma como 0
soma = 0
numero = 0

while (numero >= 0):

    numero = int(input("Digite um número: "))
    
    if numero < 0:
        break
    
    soma += numero
    
print(f"A soma dos números positivos é: {soma}")