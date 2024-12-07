# Crie uma classe Filme com os atributos titulo, genero e duracao (em minutos).
# Implemente um método especial para exibir os detalhes do filme de forma legível.

class Filme:
    def __init__(self, titulo, genero, duracao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao


    def __str__(self):
        return f"Filme: {self.titulo}, Gênero: {self.genero}, Duração: {self.duracao} minutos"


# Exemplo de uso
filme = Filme("Inception", "Ficção Científica", 148)
print(filme)
