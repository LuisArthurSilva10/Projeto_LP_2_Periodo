from singletonProdutos import repoProdutos

if not repoProdutos.listar():
    print("Nenhum produto cadastrado.")
else:
    for produtos in repoProdutos:
        print(produtos)
