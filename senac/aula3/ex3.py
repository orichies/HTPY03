# Implemente funções que gerenciam um sistema de lista de alunos:
# Adicionar um aluno.
# Remover um aluno.
# Exibir todos os alunos.

# Lista para armazenar os nomes dos alunos
lista_alunos = []

# Função para adicionar um aluno
def adicionar_aluno(nome):
    lista_alunos.append(nome)
    print(f"Aluno '{nome}' adicionado com sucesso!")

# Função para remover um aluno
def remover_aluno(nome):
    if nome in lista_alunos:
        lista_alunos.remove(nome)
        print(f"Aluno '{nome}' removido com sucesso!")       
    else:
        print(f"Erro: Aluno '{nome}' não encontrado na lista.")

# Função para exibir todos os alunos
def exibir_alunos():
    if lista_alunos:
        print("Lista de alunos:")
        for idx, aluno in enumerate(lista_alunos, start=1):
            print(f"{idx}. {aluno}")
    else:
        print("Nenhum aluno na lista.")

# Exemplo de uso
while True:
    print("\nGerenciamento de Alunos:")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Exibir Alunos")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        adicionar_aluno(nome)

    elif opcao == "2":
        nome = input("Digite o nome do aluno a ser removido: ")
        remover_aluno(nome)

    elif opcao == "3":
        exibir_alunos()

    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

