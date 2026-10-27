from itertools import count

geradorIdProduto=count(1)

def proximoIdProduto():
     return next(geradorIdProduto)


class Produto:  
    def __init__(self,nome,preco,quantidade):
        self.id=proximoIdProduto()
        self.nome=nome
        self.quantidade=quantidade
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Quantidade: Und. {self.quantidade}"

geradorIdOrdem=count(1)

def proximoIdOrdem():
     return next(geradorIdOrdem)
      
class OrdemDeServico:

    def __init__(self,nome,preco):
        self.id=proximoIdOrdem() 
        self.nome=nome
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Ordem de Serviço: {self.nome} | Preço: R$ {self.preco:.2f}"


geradorIdCliente=count(1)

def proximoIdCliente():
     return next(geradorIdCliente)

class Cliente:
    def __init__(self,nome,contato,cpf):
        self.id=proximoIdCliente()
        self.nome=nome
        self.contato=contato
        self.cpf=cpf
    def __str__(self):
          return f"Id: {self.id} || Cliente: {self.nome} | Contato: {self.contato} | Cpf: {self.cpf}"

geradorIdVendaProduto=count(1)

def proximoIdVendaProduto():
     return next(geradorIdVendaProduto)

class VendaProduto:
    def __init__(self,cliente,produto,quantidade):
        self.id=proximoIdVendaProduto()
        self.cliente=cliente
        self.produto=produto
        self.quantidade=quantidade

geradorIdVendaOrdem=count(1)
def proximoIdVendaOrdem():
     return next(geradorIdVendaOrdem)

class VendaOrdem:
    def __init__(self,cliente,servico):
        self.id=proximoIdVendaOrdem()
        self.cliente=cliente
        self.servico=servico

        
