class Conta:
    def __init__(self, titular: str, numero: int, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo


    def exibir_saldo(self):
        print(f"Titular: {self.titular}, Conta: {self.numero}, Saldo: R${self.saldo:.2f}")


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")


    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")


    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.titular}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor da transferência deve ser positivo.")


# Criando contas para testes
conta1 = Conta("João", 12345, 1000)
conta2 = Conta("Maria", 67890, 500)


# Testando operações
conta1.exibir_saldo()
conta1.depositar(200)
conta1.sacar(300)
conta1.transferir(400, conta2)
conta1.exibir_saldo()
conta2.exibir_saldo()


