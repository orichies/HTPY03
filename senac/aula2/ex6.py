# Exercício 6: Média de Números Positivos
# Escreva um programa que receba números inteiros até que o usuário digite 0. Calcule e exiba a média dos números positivos digitados.

# Inicializa a soma como 0
soma = 0
numero = 1
contagem = 0

while (numero >= 1):

    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma += numero
    contagem += 1

media = soma / contagem
    
print(f"A média dos números positivos é: {media}")
