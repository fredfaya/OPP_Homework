class Livro:
    def __init__(self, nome ,stock,preco,autores = []):
        self.nome = nome
        self.stock = stock
        self.preco = preco
        self.autores = autores
        self.autores = set(autores)

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

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_num_autores(self):
        return self.autores

    def set_autores(self, autores):
        self.autores = autores

    def get_autores(self):
        return self.autores

    def add_autor(self, autor):
        self.autores.add(autor)

    def preco_venda(self):
        return self.preco * 1.06

    def __str__(self):
        return f"{self.nome} estoque: {self.stock}, preço: {self.preco}, preco devenda: {self.preco * 1.06}"
