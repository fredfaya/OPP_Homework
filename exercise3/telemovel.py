class Telemovel:
    def __init__(self,marca,modelo,stock,preco):
        self.stock = stock
        self.preco = preco
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo} estoque: {self.stock}, preço: {self.preco}, preco de venda : {self.preco * 1.23}"
