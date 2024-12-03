# Exercício 7: Média salarios
# Escreva um programa para ler o salário e o sexo de vários funcionários (defina uma cláusula para terminar a leitura) ao término, informar a média de salário de homens e mulheres:

# Inicializa as variáveis para somar salários e contar os funcionários de cada sexo:

salariomasc = 0
salariofem = 0
masculino = 0
feminino = 0

while True:
    genero = input("DIGITE O GENÊRO DO FUNCIONÁRIO SABENDO QUE: [M] PARA MASCULINO / [F] PARA FEMININO / [S] PARA SAIR: ").strip().upper()
    
    if genero == 'S':
        break
    
    salario = float(input("DIGITE O SALÁRIO DO FUNCIONÁRIO: "))
    
    if genero == 'M':
        salariomasc += salario
        masculino += 1

    elif genero == 'F':
        salariofem += salario
        feminino += 1

    else:
        print("ERRO! DIGITE APENAS [M] OU [F]. ")

if salariomasc > 0:
    salariohomens = salariomasc / masculino
    print(f"MÉDIA SALARIAL DOS HOMENS: R${salariohomens:.2f} REAIS. ")
else:
    print("NÃO FORAM REGISTRADOS SALÁRIOS DE HOMENS NESTA EMPRESA.")

if salariofem > 0:
    salariomulheres = salariofem / feminino
    print(f"MÉDIA SALARIAL DAS MULHERES: R${salariomulheres:.2f} REAIS. ")
else:
    print("NÃO FORAM REGISTRADOS SALÁRIOS DE MULHERES NESTA EMPRESA.")
