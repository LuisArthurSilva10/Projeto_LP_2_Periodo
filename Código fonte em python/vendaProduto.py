from consultaProduto import sistema
from classes import Estoque
from itertools import count

class vendaDeProduto:
    _ids=count(1)
    def __init__(self,cliente,produto,data,quantidade):
        self.id=next(vendaDeProduto._ids)
        self.cliente=cliente 
        self.produto=produto
        self.quantidade=quantidade
        self.data=data 
    def __str__(self):
            return f"Id: {self.id} || Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Quantidade: Und. {self.quantidade}"

class data:
     def __init__(self,dia,mes,ano):
          self.dia=dia
          self.mes=mes
          self.ano=ano
     def __str__(self):
       return f"{self.dia}/{self.mes}/{self.ano}"

def funcaoVendaProduto():
    print("Selecione com base no ID o produto vendido: \n")
    sistema.exibicao()
    opcaoProduto=int(input())
    produtoSelecionado=Estoque.buscarPorId(opcaoProduto)
    print("Digite a quantidade vendida do produto: ")
    qntVendida=int(input())
    if(produtoSelecionado.quantidade<qntVendida):
         print("Estoque insuficiente.")
         return
    produtoSelecionado.quantidade -=qntVendida
    total= qntVendida * produtoSelecionado.preco
    dataProduto=data
    print("Digite o ano da venda: ")
    ano=int(input())
    dataProduto.ano=ano
    print("Digite o mês da venda: ")
    mes=int(input())
    dataProduto.mes=mes
    print("Digite o dia da venda: ")
    dia=int(input())
    dataProduto.dia=dia
    vendaDeProduto.data=dataProduto

    print("Escolha com base no ID o comprador: ")

            





