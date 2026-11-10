from singletonVendasProdutos import repoVendasProdutos
from singletonCliente import repoClientes

def funcaoVendaProduto():
        print("Opções de consulta das vendas: ")
        print("1-Consulta geral")
        print("2-Consulta com cliente")
        print("3-Consulta com tempo")
        opcao=int(input())
        if(opcao==1):
            for v in repoVendasProdutos.listar():
                print(v)
        elif(opcao==2):
            print("Escolha com base no ID o cliente que deseja consultar: ")
            for c in repoClientes.listar():
                print(c)
            opcaoCliente=int(input())
            clienteSelecionado = repoClientes.buscar_por_id(opcaoCliente)
            if clienteSelecionado is None:           
                print("Cliente não encontrado.")
                return             
            vendas = repoVendasProdutos.buscar_por_cliente(clienteSelecionado)
            if not vendas:
                print("Nenhuma venda seleciondada")
            else:
                for v in vendas:
                    print(v)
