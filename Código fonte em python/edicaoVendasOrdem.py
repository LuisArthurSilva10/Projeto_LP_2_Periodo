from singletonVendasOrdem import repoVendasServico
from singletonOrdem import repoServico
from singletonCliente import repoClientes
from classes import Data

def funcaoEdicaoVendasOrdem():
  while True:
    print("Escolha com base no id a venda de ordem que deseja alterar: ")

    for p in repoVendasServico.listar():
       print(p)
    escolha=int(input())
    vendaServicoEscolhida=repoVendasServico.buscar_por_id(escolha)
    print("O que deseja alterar: ")
    print("1-Ordem")
    print("2-Comprador")
    print("3-Data")
    print("4-Remover")
    opcaoEdicao=int(input())
    if(opcaoEdicao==1):
       print("Digite qual ordem de serviço foi escolhida pelo comprador: ")

       if not repoServico.listar():
          print("Nenhuma ordem cadastrada.")
       else:
          for s in repoServico.listar():
             print(s)
          escolhaServico=int(input())
          servicoEscolhido=repoServico.buscar_por_id(escolhaServico)
          vendaServicoEscolhida.servico=servicoEscolhido
          print("Venda de Ordem de serviço alterada com sucesso.")

    elif(opcaoEdicao==2):
       print("Digite qual cliente é o comprador: ")

       if not repoClientes.listar():
          print("Nenhum cliente cadastrado.")
       else:
          for s in repoClientes.listar():
             print(s)
          escolhaCliente=int(input())
          clienteEscolhido=repoClientes.buscar_por_id(escolhaCliente)
          vendaServicoEscolhida.cliente=clienteEscolhido
          print("Venda de Ordem de serviço alterada com sucesso.")
    
    elif(opcaoEdicao==3):
      dataNova=Data()
      print("Digite o ano: ")
      ano=int(input())
      print("Digite o mês: ")
      mes=int(input())
      print("Digite o dia: ")
      dia=int(input())
      vendaServicoEscolhida.data=dataNova(dia,mes,ano)
      print("Produto editado com sucesso.")

    elif(opcaoEdicao==4):
          repoVendasServico.remover(escolha)
    print("Deseja editar outra venda de Ordem de serviço?(s/n)")
    escolhaLoop=input()
    if(escolhaLoop!="s"):
      break 


