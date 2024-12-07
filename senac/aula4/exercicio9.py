# Crie uma classe Funcionario com os atributos nome, horas_trabalhadas e valor_hora.
# Adicione os métodos:
# registrar_horas(horas) para registrar horas trabalhadas.
# calcular_pagamento() para calcular o pagamento baseado nas horas trabalhadas e no valor por hora.

class Funcionario:
    def __init__(self, nome, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = 0
        self.valor_hora = valor_hora


    def registrar_horas(self, horas):
        self.horas_trabalhadas += horas
        print(f"{horas} hora(s) registrada(s) para {self.nome}.")


    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora


# Exemplo de uso
funcionario = Funcionario("Maria", 20)
funcionario.registrar_horas(8)
funcionario.registrar_horas(5)
print(f"Pagamento: R${funcionario.calcular_pagamento():.2f}")
