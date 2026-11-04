from consultaProduto import sistemaConsultaProdutos
from consultaCliente import sistemaConsultaCliente
from cadastroProduto import sistemaEstoque
from cadastroCliente import sistemaClientesIndexados

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
            return f"Id: {self.id} || Produto: {self.produto} | Comprador:  {self.cliente} | Quantidade: Und. {self.quantidade} | Data: Und. {self.data}"

class cadastroVendaProduto:
    def __init__(self):
        self.listaVendaProduto=[]
    def cadastro(self,vendaProduto):
        self.listaVendaProduto.append(vendaProduto)
        print("\nCadastro feito com sucesso\n")
    def exibicao(self):
        print("\n\n==Lista de vendas de produtos cadastradas==")
        if not self.listaVendaProduto:
            print("Nenhuma venda cadastrada")
            return
        for vendaDeProduto in self.listaVendaProduto:
            print(f"{vendaDeProduto}")
    #def commit(self):
     #   sistema.lista.extend(self.listaClientes)

class data:
     def __init__(self,dia,mes,ano):
          self.dia=dia
          self.mes=mes
          self.ano=ano
     def __str__(self):
       return f"{self.dia}/{self.mes}/{self.ano}"

sistemaVendaProdutos=cadastroVendaProduto()

def funcaoVendaProduto():
    
   while True: 
    print("Selecione com base no ID o produto vendido: \n")
    sistemaConsultaProdutos.exibicao()
    opcaoProduto=int(input())
    produtoSelecionado=sistemaEstoque.buscarPorId(opcaoProduto)
    
    print("Digite a quantidade vendida do produto: ")
    qntVendida=int(input())
    if(produtoSelecionado.quantidade<qntVendida):
         print("Estoque insuficiente.")
         return
    
    produtoSelecionado.quantidade -=qntVendida
    total= qntVendida * produtoSelecionado.preco
    

    print("Digite o ano da venda: ")
    ano=int(input())
    print("Digite o mês da venda: ")
    mes=int(input())
    print("Digite o dia da venda: ")
    dia=int(input())
    dataProduto=data(dia,mes,ano)

    print("Escolha com base no ID o comprador: ")
    sistemaConsultaCliente.exibicao()
    opcaoCliente=int(input())
    clienteSelecionado=sistemaClientesIndexados.buscarPorId(opcaoCliente)

    vendaCadastrada=vendaDeProduto(clienteSelecionado,produtoSelecionado,dataProduto,qntVendida)
    sistemaVendaProdutos.cadastro(vendaCadastrada)
    print("Deseja cadastrar outra venda?(s/n): ")
    opcao=input().lower()
    if(opcao !="s"):
        break
        
   sistemaVendaProdutos.exibicao()


            





