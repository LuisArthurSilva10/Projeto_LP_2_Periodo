from singletonOrdem import repoServico
from singletonCliente import repoClientes
import cadastroCliente
import cadastroOrdem
from singletonVendasOrdem import repoVendasServico
from classes import vendaDeServico, Data

def funcaoVendaOrdem():
    while True:
        print("\nEscolha com base no ID o comprador:")
        print("(0 para cadastrar novo cliente)")
        for c in repoClientes.listar():
            print(c)

        try:
            opcaoCliente = int(input())
        except ValueError:
            print("ID inválido.")
            continue

        if opcaoCliente == 0:
            cadastroCliente.funcaoCadastroCliente()
            continue

        clienteSelecionado = repoClientes.buscar_por_id(opcaoCliente)
        
        if clienteSelecionado is None:           
            print("Cliente não encontrado.")
            continue
        break
    
    while True:
        print("\nSelecione com base no ID a ordem de serviço contratada:")
        print("(0 para cadastrar nova ordem de serviço)")

        for s in repoServico.listar():
            print(s)
        try:
            opcaoOrdem= int(input())
        except ValueError:
            print("ID inválido.")
            continue
        if opcaoOrdem==0:
            cadastroOrdem.funcaoCadastroOrdem()
            continue

        servicoSelecionado = repoServico.buscar_por_id(opcaoOrdem)

        if servicoSelecionado  is None:           
            print("Servico não encontrado.")
            continue

        try:
            ano = int(input("Digite o ano da venda: "))
            mes = int(input("Digite o mês da venda: "))
            dia = int(input("Digite o dia da venda: "))
        except ValueError:
            print("Data inválida.")
            continue

        dataProduto = Data(dia, mes, ano)


        vendaCadastrada = vendaDeServico(
            clienteSelecionado.nome,
            servicoSelecionado.nome,
            dataProduto,
            servicoSelecionado.preco
            
        )

        if repoVendasServico.adicionar(vendaCadastrada):
            print("Venda de ordem registrada com sucesso.")
        else:
            print("ID de venda duplicado.")

        if input("Deseja cadastrar outra venda? (s/n): ").lower() != "s":
            break

    print("\n==Lista de vendas cadastradas==")
    vendas = repoVendasServico.listar()
    if not vendas:
        print("Nenhuma venda cadastrada")
    else:
        for v in vendas:
            print(v)
