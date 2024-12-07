# Crie uma classe Livro com os atributos titulo, autor e ano_publicacao.
# Adicione um método verificar_antiguidade(ano_atual) que retorna se o livro é considerado antigo (mais de 50 anos).
# Use __str__ para exibir as informações do livro.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


    def verificar_antiguidade(self, ano_atual):
        return ano_atual - self.ano_publicacao > 50


    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}"


# Exemplo de uso
livro = Livro("Dom Casmurro", "Machado de Assis", 1899)
print(livro)
print("Livro antigo:", livro.verificar_antiguidade(2024))