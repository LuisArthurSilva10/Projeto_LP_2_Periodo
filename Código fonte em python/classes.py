from itertools import count

class Produto:
    _ids=count(1)  
    def __init__(self,nome,preco,quantidade):
        self.id=next(Produto._ids)
        self.nome=nome
        self.quantidade=quantidade
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Produto: {self.nome} | Preço: R$ {self.preco:.2f} | Quantidade: Und. {self.quantidade}"

class Estoque:
    def __init__(self):
        self.produtos={}
    def adicionar(self, produtosClasse=Produto):
        self.produtos[produtosClasse.id]=produtosClasse
    def buscarPorId(self,idProduto:int):
        return self.produtos.get(idProduto)
    def repor(self,idProduto:int,qnt:int):
        p=self.buscarPorId(idProduto)
        if p:
            p.quantidade+=qnt
            print(f"Reposto +{qnt} |Produto:{p.nome}| total: {p.quantidade}")
        else:
            print("Produto não encontrado.")


class OrdemDeServico:
    _ids=count(1)
    def __init__(self,nome,preco):
        self.id=next(OrdemDeServico._ids) 
        self.nome=nome
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Ordem de Serviço: {self.nome} | Preço: R$ {self.preco:.2f}"

class Cliente:
    _ids=count(1)
    def __init__(self,nome,contato,cpf):
        self.id=next(Cliente._ids)
        self.nome=nome
        self.contato=contato
        self.cpf=cpf
    def __str__(self):
          return f"Id: {self.id} || Cliente: {self.nome} | Contato: {self.contato} | Cpf: {self.cpf}"

class ClientesIndexados:
    def __init__(self):
        self.clientes={}
    def adicionar(self, clientesClasse=Cliente):
        self.clientes[clientesClasse.id]=clientesClasse
    def buscarPorId(self,idClientes:int):
        return self.clientes.get(idClientes)
