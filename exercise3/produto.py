class Produto:
    def __init__(self,nome,stock,preco):
        self.nome = nome
        self.stock = stock
        self.preco = preco

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock

    def get_preco_base(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco