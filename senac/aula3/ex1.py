# Crie uma função cumprimentar que receba o nome e a hora do dia e retorne uma mensagem personalizada Bom dia, Boa tarde ou Boa noite.

def cumprimentar(nome, hora):
    if hora < 12:
        print("Bom Dia, Sr.", nome)

    elif hora < 18:
        print("Boa Tarde, Sr.", nome)

    else:
        print("Boa Noite Sr.", nome)

name = input("Digite Seu Nome: ")
hour = int(input("Que Horas São? "))

cumprimentar(name, hour)

