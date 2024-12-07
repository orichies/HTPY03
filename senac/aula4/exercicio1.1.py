# Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} Anos.")

# Coletando informações do usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))  # Converte para inteiro

# Criando uma instância da classe Pessoa com os dados do usuário
pessoa1 = Pessoa(nome, idade)

# Exibindo as informações da pessoa
pessoa1.exibir_informacoes()