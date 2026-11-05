from itertools import count

class Produto:
    _ids=count(1)  
    def __init__(self,nome,preco,quantidade):
        self.id=next(Produto._ids)
        self.nome=nome
        self.quantidade=quantidade
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Produto: {self.nome} || Preço: R$ {self.preco:.2f} || Quantidade: Und. {self.quantidade}"

class RepositorioProdutos:
    def __init__(self):
        self._produtos = {} 

    def adicionar(self, produto) -> bool:
        if produto.id in self._produtos:                
            return False   
        self._produtos[produto.id] = produto            
        return True

    def remover(self, id_produto) -> bool:
        return self._produtos.pop(id_produto, None) is not None

    def buscar_por_id(self,  id_produto):
        return self._produtos.get( id_produto)            

    def buscar_por_nome(self, trecho):
        trecho = trecho.lower()
        return [c for c in self._produtos.values() if trecho in c.nome.lower()]

    def listar(self):
        return list(self._produtos.values())

    def __len__(self):
        return len(self._produtos)

class OrdemDeServico:
    _ids=count(1)
    def __init__(self,nome,preco):
        self.id=next(OrdemDeServico._ids) 
        self.nome=nome
        self.preco=preco
    def __str__(self):
        return f"Id: {self.id} || Ordem de Serviço: {self.nome} || Preço: R$ {self.preco:.2f}"

class RepositorioServico:
    def __init__(self):
        self._servico = {} 

    def adicionar(self, servico) -> bool:
        if servico.id in self._servico:                
            return False                                
        self._servico[servico.id] = servico            
        return True

    def remover(self, id_servico) -> bool:
        return self._servico.pop(id_servico, None) is not None

    # ---------- CONSULTAR (leitura) ----------
    def buscar_por_id(self, id_servico):
        return self._servico.get(id_servico)            # O(1) via índice

    def buscar_por_nome(self, trecho):
        trecho = trecho.lower()
        return [c for c in self._servico.values() if trecho in c.nome.lower()]

    def listar(self):
        return list(self._servico.values())             # visão derivada

    def __len__(self):
        return len(self._servico)


class Cliente:
    _ids=count(1)
    def __init__(self,nome,contato,cpf):
        self.id=next(Cliente._ids)
        self.nome=nome
        self.contato=contato
        self.cpf=cpf
    def __str__(self):
          return f"Id: {self.id} || Cliente: {self.nome} || Contato: {self.contato} || Cpf: {self.cpf}"

class RepositorioClientes:
    def __init__(self):
        self._clientes = {} 

    def adicionar(self, cliente) -> bool:
        if cliente.id in self._clientes:                
            return False
        if cliente.cpf != "0" and self.buscar_por_cpf(cliente.cpf):
            return False                                
        self._clientes[cliente.id] = cliente            
        return True

    def remover(self, id_cliente) -> bool:
        return self._clientes.pop(id_cliente, None) is not None

    # ---------- CONSULTAR (leitura) ----------
    def buscar_por_id(self, id_cliente):
        return self._clientes.get(id_cliente)            # O(1) via índice

    def buscar_por_cpf(self, cpf):
        return next((c for c in self._clientes.values() if c.cpf == cpf), None)

    def buscar_por_nome(self, trecho):
        trecho = trecho.lower()
        return [c for c in self._clientes.values() if trecho in c.nome.lower()]

    def listar(self):
        return list(self._clientes.values())             # visão derivada

    def __len__(self):
        return len(self._clientes)

class vendaDeProduto:
    _ids=count(1)
    def __init__(self,cliente,produto,data,quantidade,total):
        self.id=next(vendaDeProduto._ids)
        self.cliente=cliente 
        self.produto=produto
        self.quantidade=quantidade
        self.data=data 
        self.total=total
    def __str__(self):
            return f"\nId Venda: {self.id} || Produto: {self.produto} || Comprador:  {self.cliente} || Quantidade: Und. {self.quantidade} || Data:{self.data} Total: R$ {self.total}"

class Data:
     def __init__(self,dia,mes,ano):
          self.dia=dia
          self.mes=mes
          self.ano=ano
     def __str__(self):
       return f"{self.dia}/{self.mes}/{self.ano}"

class RepositorioVendas:
    def __init__(self):
        self._vendas = {}          # id -> vendaDeProduto  (fonte única)

    # ---------- INDEXAR (escrita) ----------
    def adicionar(self, venda) -> bool:
        if venda.id in self._vendas:                 # já indexada?
            return False
        self._vendas[venda.id] = venda               # indexa e guarda
        return True

    def remover(self, id_venda) -> bool:
        return self._vendas.pop(id_venda, None) is not None

    # ---------- CONSULTAR (leitura) ----------
    def buscar_por_id(self, id_venda):
        return self._vendas.get(id_venda)            # O(1) via índice

    def buscar_por_cliente(self, cliente):
        """Todas as vendas de um cliente (por id do cliente)."""
        return [v for v in self._vendas.values()
                if getattr(v, "cliente", None) is not None
                and v.cliente.id == cliente.id]

    def listar(self):
        return list(self._vendas.values())           # visão derivada

    def __len__(self):
        return len(self._vendas)
