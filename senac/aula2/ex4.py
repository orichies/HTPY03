# Exercício 4: Tabuada
# Escreva um programa que exiba a tabuada de multiplicação de um número digitado pelo usuário, de 1 a 10.

numero = int(input(" digite o número: "))

for i in range(1, 11):
    print(f" {numero} x {i} = {numero*i} ")
