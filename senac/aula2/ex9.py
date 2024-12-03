# Exercício 9: Contagem de Parcelas
# Crie um programa que calcule o valor total de uma compra feita em várias parcelas. Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. 
# Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.

parcelas = int(input("QUANTAS PARCELAS? "))
totalparcelas = float(input("DIGITE O VALOR DA PARCELA:"))

total = parcelas * totalparcelas

if total > 1000:
    total += total * 0.05

print(f"Valor total a pagar: R$ {total:.2f}")
