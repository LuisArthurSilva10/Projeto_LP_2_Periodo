from classes import Produto
from singletonProdutos import repoProdutos

def funcaoCadastroProduto():
    while True:
        nome    = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade de unidades do produto): "))

        produto = Produto(nome,preco,quantidade)

        if repoProdutos.adicionar(produto):
            print("Cadastro feito com sucesso.")
        else:
            print("Produto já cadastrado (ID duplicado).")

        if input("Deseja cadastrar outro cliente? (s/n): ") != "s":
            break

    print("\n==Lista de produtos cadastrados==")
    for p in repoProdutos.listar():
        print(p)
    return
