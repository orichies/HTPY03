# Crie uma classe ReservaHotel com os atributos nome_cliente, dias_reserva e valor_diaria.
# Adicione os métodos:
# calcular_valor_total() para calcular o valor total da reserva.
# Um método especial __str__ para exibir os detalhes da reserva.

class ReservaHotel:
    def __init__(self, nome_cliente, dias_reserva, valor_diaria):
        self.nome_cliente = nome_cliente
        self.dias_reserva = dias_reserva
        self.valor_diaria = valor_diaria


    def calcular_valor_total(self):
        return self.dias_reserva * self.valor_diaria


    def __str__(self):
        return f"Reserva: Cliente: {self.nome_cliente}, Dias: {self.dias_reserva}, Total: R${self.calcular_valor_total():.2f}"


# Exemplo de uso
reserva = ReservaHotel("João", 5, 200)
print(reserva)