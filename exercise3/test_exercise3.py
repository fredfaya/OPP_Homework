from exercise3.eletrodomestico import Eletrodoméstico
from exercise3.livro import Livro
from exercise3.telemovel import Telemovel
from exercise3.televisor import Televisor


def teste():
    livro1 = Livro("Livro 1", 100, 15.0)  # nome, stock, preço
    livro1.add_autor("Autor 1")
    livro1.add_autor("Autor 2")
    print(f"{livro1.get_nome()} tem {len(livro1.get_autores())} autores")
    lista = []
    lista.append("Autor X")
    lista.append("Autor Y")
    lista.append("Autor Z")
    livro2 = Livro("Livro 2", 0, 23.0, lista)
    livro2.set_stock(450);
    print(f"{livro2.get_nome()} tem {len(livro2.get_num_autores())} autores")
    tlv1 = Televisor("Sony", "KX1188", 3, 1000)  # marca, modelo, stock, preco
    tlm1 = Telemovel("XWZ", "Model A", 13, 560.0)  # marca, modelo, quantidade, preço
    electr1 = Eletrodoméstico("Frigorífico", 2, 780)
    electr2 = Eletrodoméstico("Fogão", 1, 423)
    # electr1.set_classe("A+");
    # adicionar a lista com produtos na loja
    lista_produtos = [livro1, livro2, electr1, electr2, tlv1, tlm1]
    # lista todos os produtos, com preços, numa tabela
    print("Lista de Todos os Produtos:")
    for prod in lista_produtos:
        print(prod)


if __name__ == "__main__":
    teste()
