from singletonProdutos import repoProdutos
def funcaoConsultaProdutos():
 if not repoProdutos.listar():
     print("Nenhum produto cadastrado.")
 else:
    for produtos in repoProdutos.listar():
        print(produtos)
