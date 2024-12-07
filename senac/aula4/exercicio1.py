# Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

pessoa1 = Pessoa("Richard", 21)
pessoa1.exibir_informacoes()  # Saída: Richard 21


