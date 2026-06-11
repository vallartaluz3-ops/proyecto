class Pedido:
    def __init__(self, numero, combo):
        self.numero = numero
        self.combo = combo

    def __str__(self):
        return f"Pedido #{self.numero} - {self.combo}"