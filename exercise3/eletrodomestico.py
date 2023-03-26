class Eletrodoméstico:
    def __init__(self, nome,stock,preco):
        self.nome = nome
        self.stock = stock
        self.preco = preco

    def __str__(self):
        return f"{self.nome} estoque: {self.stock}, preço: {self.preco}, preco de venda : {self.preco * 1.23}"