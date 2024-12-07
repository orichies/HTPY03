class Animal:
    def __init__(self, nome):
        self.nome = nome


class Cachorro(Animal):
    def som(self):
        return "Au au!"


class Gato(Animal):
    def som(self):
        return "Miau!"


dog = Cachorro("Rex")
cat = Gato("Felix")
print(dog.nome, dog.som())  # Saída: Au au!
print(cat.nome, cat.som())  # Saída: Miau!
