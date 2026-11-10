from singletonProdutos import repoProdutos
from singletonCliente import repoClientes
import cadastroCliente
from singletonVendasProdutos import repoVendasProdutos
from classes import vendaDeProduto, Data

def funcaoVendaProduto():
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

        print("\nSelecione com base no ID o produto vendido:")

        for p in repoProdutos.listar():
            print(p)
        try:
            opcaoProduto = int(input())
        except ValueError:
            print("ID inválido.")
            continue

        produtoSelecionado = repoProdutos.buscar_por_id(opcaoProduto)

        if produtoSelecionado is None:           
            print("Produto não encontrado.")
            continue

        try:
            qntVendida = int(input("Digite a quantidade vendida: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        if produtoSelecionado.quantidade < qntVendida:
            print("Estoque insuficiente.")
            continue                            

        produtoSelecionado.quantidade -= qntVendida
        total = qntVendida * produtoSelecionado.preco

        try:
            ano = int(input("Digite o ano da venda: "))
            mes = int(input("Digite o mês da venda: "))
            dia = int(input("Digite o dia da venda: "))
        except ValueError:
            print("Data inválida.")
            produtoSelecionado.quantidade += qntVendida   # desfaz baixa
            continue

        dataProduto = Data(dia, mes, ano)

        vendaCadastrada = vendaDeProduto(
            clienteSelecionado,
            produtoSelecionado,
            dataProduto,
            qntVendida,
            total,
        )

        if repoVendasProdutos.adicionar(vendaCadastrada):
            print("Venda registrada com sucesso.")
        else:
            print("ID de venda duplicado.")

        if input("Deseja cadastrar outra venda? (s/n): ").lower() != "s":
            break

    print("\n==Lista de vendas cadastradas==")
    vendas = repoVendasProdutos.listar()
    if not vendas:
        print("Nenhuma venda cadastrada")
    else:
        for v in vendas:
            print(v)
