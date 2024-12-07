# Crie uma classe Livro com atributos titulo e autor. 
# Sobrescreva o método especial __str__ para que, ao usar print em um objeto da classe, ele exiba o título e o autor do livro no formato: "Título: <titulo>, Autor: <autor>"

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Título: {self.titulo} / Autor: ({self.autor})"

nome = Livro("Python Para Iniciantes", "Richard Roch")
print(nome)   


