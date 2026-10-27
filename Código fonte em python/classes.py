from itertools import count

geradorId=count(1)

def proximoId():
    return next(geradorId)


class Produto:
    def __init__(self,nome,preco,quantidade):
        self.id=proximoId()
        self.nome=nome
        self.quantidade=quantidade
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Quantidade: Und. {self.quantidade}"
        
class OrdemDeServico:

    def __init__(self,nome,preco):
        self.id=proximoId() 
        self.nome=nome
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Ordem de Serviço: {self.nome} | Preço: R$ {self.preco:.2f}"

class Cliente:
    def __init__(self,nome,contato,cpf):
        self.id=proximoId()
        self.nome=nome
        self.contato=contato
        self.cpf=cpf
    def __str__(self):
          return f"Id: {self.id} || Cliente: {self.nome} | Contato: {self.contato} | Cpf: {self.cpf}"

class VendaProduto:
    def __init__(self,cliente,produto,quantidade):
        self.id=proximoId
        self.cliente=cliente
        self.produto=produto
        self.quantidade=quantidade

class VendaOrdem:
    def __init__(self,cliente,servico):
        self.id=proximoId
        self.cliente=cliente
        self.servico=servico

        
