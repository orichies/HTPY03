# Exercício 8 : Cálculo IRPF
# Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário.

# No Brasil, a tabela do Imposto de Renda para pessoas físicas (IRPF) é progressiva, ou seja, as alíquotas aumentam conforme a renda do contribuinte. 
# A tabela é ajustada anualmente e varia de acordo com a faixa de salário. Para o ano de 2024, as faixas de tributação do Imposto de Renda para pessoas físicas são as seguintes:

# Até R$ 2.112,00: isento (não paga imposto de renda)
# De R$ 2.112,01 até R$ 2.826,65: 7,5% (aplica-se sobre o valor que exceder a R$ 2.112,00)
# De R$ 2.826,66 até R$ 3.751,05: 15% (aplica-se sobre o valor que exceder a R$ 2.826,65)
# De R$ 3.751,06 até R$ 4.664,68: 22,5% (aplica-se sobre o valor que exceder a R$ 3.751,05)
# Acima de R$ 4.664,68: 27,5% (aplica-se sobre o valor que exceder a R$ 4.664,68)

def calcular_irpf(salario):
    if salario <= 1903.98:
        imposto = 0
    elif salario <= 2826.65:
        imposto = salario * 0.075
    elif salario <= 3751.05:
        imposto = salario * 0.15
    elif salario <= 4664.68:
        imposto = salario * 0.225
    else:
        imposto = salario * 0.275
    return imposto

salario = float(input("Informe o salário do funcionário: R$ "))

imposto = calcular_irpf(salario)

print(f"O valor do IRPF a ser descontado é: R$ {imposto:.2f}")