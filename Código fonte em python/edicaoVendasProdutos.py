from singletonVendasProdutos import repoVendasProdutos
from singletonProdutos import repoProdutos
from singletonCliente import repoClientes
from classes import Data



def funcaoEdicaoVendasProdutos():
  while True:
    print("Escolha com base no id a venda de ordem que deseja alterar: ")

    for p in repoVendasProdutos.listar():
       print(p)
    escolha=int(input())
    vendaProdutoEscolhida=repoVendasProdutos.buscar_por_id(escolha)
    print("O que deseja alterar: ")
    print("1-Produto")
    print("2-Quantidade")
    print("3-Comprador")
    print("4-Data")
    print("5-Remover")
    opcaoEdicao=int(input())
    if(opcaoEdicao==1):
        print("Digite qual produto foi comprado pelo comprador: ")
       
        if not repoProdutos.listar():
           print("Nenhum produto cadastrado.")
        else:
          for p in repoProdutos.listar():
             print(p)
          escolhaProduto=int(input())
          produtoEscolhido=repoProdutos.buscar_por_id(escolhaProduto)
          vendaProdutoEscolhida.produto=produtoEscolhido
          print("Venda de Ordem de serviço alterada com sucesso.")

    elif(opcaoEdicao==2):
       
       print("Digite qual quantidade foi comprada pelo comprador: ")
       quantidadeAtual=int(input())
       if(quantidadeAtual>0):
          vendaProdutoEscolhida.produto.quantidade+=vendaProdutoEscolhida.quantidade
          vendaProdutoEscolhida.quantidade=quantidadeAtual
          vendaProdutoEscolhida.produto.quantidade-=vendaProdutoEscolhida.quantidade
          vendaProdutoEscolhida.total=vendaProdutoEscolhida.produto.preco*vendaProdutoEscolhida.quantidade
          break

    elif(opcaoEdicao==3):
        print("Digite qual é o comprador: ")
             
        if not repoClientes.listar():
           print("Nenhum cliente cadastrado.")
        else:
          for c in repoClientes.listar():
            print(c)
          escolhaCliente=int(input())
          clienteEscolhido=repoClientes.buscar_por_id(escolhaCliente)
          vendaProdutoEscolhida.cliente=clienteEscolhido
          print("Venda de Produto alterada com sucesso.")

    elif(opcaoEdicao==4):
          dataNova=Data()
          print("Digite o ano: ")
          ano=int(input())
          print("Digite o mês: ")
          mes=int(input())
          print("Digite o dia: ")
          dia=int(input())
          vendaProdutoEscolhida.data=dataNova(dia,mes,ano)
          print("Produto editado com sucesso.")

    elif(opcaoEdicao==5):
          repoVendasProdutos.remover(escolha)
    print("Deseja editar outra venda de produto?(s/n)")
    escolhaLoop=input()
    if(escolhaLoop!="s"):
      break 


