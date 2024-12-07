class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

meu_carro = Carro("Civic", 2020)
print(meu_carro.modelo, meu_carro.ano)  # Saída: Civic 2020

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Carro: {self.modelo}, Ano: {self.ano}")

meu_carro = Carro("Civic", 2020)
meu_carro.exibir_informacoes()  # Saída: Carro: Civic, Ano: 2020

