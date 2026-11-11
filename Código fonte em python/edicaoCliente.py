from singletonCliente import repoClientes

def funcaoEdicaoCliente():
  while True:
    print("Escolha com base no id o produto que deseja alterar: ")

    for p in repoClientes.listar():
       print(p)
    escolha=int(input())
    print("O que deseja alterar: ")
    print("1-Nome: ")
    print("2-Quantidade")
    print("3-Preço ")
    print("4-Remover")
    opcaoEdicao=int(input())
    if(opcaoEdicao==1):
      print("Digite o nome para alterar: ")
      repoClientes.buscar_por_id(escolha).nome=input()
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==2):
      print("Digite o contato para alterar: ")
      repoClientes.buscar_por_id(escolha).contato=input()
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==3):
      print("Digite o CPF para alterar: ")
      repoClientes.buscar_por_id(escolha).cpf=input()
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==4):
      repoClientes.remover(escolha)
      print("Produto editado com sucesso.")

    print("Deseja editar outro produto?(s/n)")
    escolhaLoop=input()
    if(escolhaLoop!="s"):
      break 


