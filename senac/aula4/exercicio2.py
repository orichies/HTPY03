# Implemente uma classe chamada Produto com:
# Atributos: nome, preco e estoque.
# Um método chamado vender que reduz o estoque ao vender o produto, se houver unidades disponíveis.
# Um método chamado repor que aumenta o estoque ao receber novas unidades.

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade > self.estoque:
            print(f"NÃO HÁ ESTOQUE SUFICIENTE PARA VENDER {quantidade} UNIDADES.")
            print(f"ESTOQUE DISPONÍVEL: {self.estoque}")
        else:
            self.estoque -= quantidade
            print(f"VENDA CONCLUÍDA: {quantidade} UNIDADES DE '{self.nome}' VENDIDAS.")
            print(f"ESTOQUE RESTANTE: {self.estoque}")

    def repor(self, quantidade):
        self.estoque += quantidade
        print(f"ESTOQUE DE '{self.nome}' FOI ATUALIZADO COM {quantidade} UNIDADES.")
        print(f"NOVO ESTOQUE: {self.estoque}")

def vendas():
    nome = input("DIGITE O NOME DO PRODUTO: ")
    preco = float(input(f"DIGITE O PREÇO DO PRODUTO '{nome}': "))
    estoque = int(input(f"DIGITE A QUANTIDADE INICIAL DE ESTOQUE PARA '{nome}': "))

    produto = Produto(nome, preco, estoque)

    while True:
        print("\n O QUE PRETENDE FAZER?")
        print("[1]: VENDER PRODUTO")
        print("[2]: REPOR ESTOQUE")
        print("[3]: VER INFORMAÇÕES DO PRODUTO")
        print("[4]: SAIR")
        escolha = input("DIGITE SUA ESCOLHA: [1] / [2] / [3] / [4]: ")

        if escolha == "1":
            quantidade = int(input(f"QUANTAS UNIDADES DE '{produto.nome}' DESEJA VENDER? "))
            produto.vender(quantidade)

        elif escolha == "2":
            quantidade = int(input(f"QUANTAS UNIDADES DE '{produto.nome}' DESEJA REPOR? "))
            produto.repor(quantidade)

        elif escolha == "3":
            print(f"\n PRODUTO: {produto.nome}")
            print(f"PREÇO: R${produto.preco:.2f} REAIS.")
            print(f"ESTOQUE ATUAL: {produto.estoque} UNIDADES.")

        elif escolha == "4":
            print("FIM DO PROGRAMA, OBRIGADO!")
            break

        else:
            print("ERRO, TENTE NOVAMENTE!")

vendas()




