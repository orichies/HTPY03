# Implemente uma função que receba dois números e uma operação (+, -, *, /) e devolva o resultado.

def calculadora():
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = num1 + num2

        elif operacao == '-':
            resultado = num1 - num2
            
        elif operacao == '*':
            resultado = num1 * num2

        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                return "Erro."
        else:
            return "Erro."
        
        return f"O resultado é: {resultado}"

print(calculadora())

