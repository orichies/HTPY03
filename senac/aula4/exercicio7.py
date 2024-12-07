# Crie uma classe Tarefa com os atributos descricao e status (inicialmente "pendente").
# Adicione métodos para:
# Alterar o status para "concluída" (marcar_como_concluida).
# Exibir os detalhes da tarefa (exibir_tarefa).

class Tarefa:
    def __init__(self, mostrar):
        self.mostrar = mostrar
        self.status = "pendente"

    def marcar_como_concluida(self):
        self.status = "concluída"

    def exibir_tarefa(self):
        print(f"Tarefa: {self.mostrar}\n Status: {self.status}")

tarefa = Tarefa(" [Finalizar Compra] ")
tarefa.exibir_tarefa()
tarefa.marcar_como_concluida()
tarefa.exibir_tarefa()
    

