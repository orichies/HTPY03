class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Maria", 25)
print(pessoa1.nome, pessoa1.idade)  # Saída: Maria 25
