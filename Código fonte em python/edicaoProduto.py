from singletonProdutos import repoProdutos

def funcaoEdicaoProduto():
  while True:
    print("Escolha com base no id o produto que deseja alterar: ")

    for p in repoProdutos.listar():
       print(p)
    escolha=int(input())
    repoProdutos.buscar_por_id(escolha)
    print("O que deseja alterar: ")
    print("1-Nome: ")
    print("2-Quantidade")
    print("3-Preço ")
    opcaoEdicao=int(input())
    if(opcaoEdicao==1):
      print("Digite o nome para alterar: ")
      repoProdutos.buscar_por_id(escolha).nome=input()
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==2):
      print("Digite a quantidade para alterar: ")
      repoProdutos.buscar_por_id(escolha).quantidade=int(input())
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==3):
      print("Digite o preço para alterar: ")
      repoProdutos.buscar_por_id(escolha).preco=float(input())
      print("Produto editado com sucesso.")

    print("Deseja editar outro produto?(s/n)")
    escolhaLoop=input()
    if(escolhaLoop!="s"):
      break 


