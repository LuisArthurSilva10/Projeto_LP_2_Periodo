from singletonOrdem import repoServico

def funcaoEdicaoOrdem():
  while True:
    print("Escolha com base no id o produto que deseja alterar: ")

    for p in repoServico.listar():
       print(p)
    escolha=int(input())
    print("O que deseja alterar: ")
    print("1-Nome: ")
    print("2-Preço")
    print("3-Remover")
    opcaoEdicao=int(input())
    if(opcaoEdicao==1):
      print("Digite o nome para alterar: ")
      repoServico.buscar_por_id(escolha).nome=input()
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==2):
      print("Digite o preço para alterar: ")
      repoServico.buscar_por_id(escolha).preco=float(input())
      print("Produto editado com sucesso.")
    elif(opcaoEdicao==3):
      repoServico.remover(escolha)
      print("Produto editado com sucesso.")
    
    print("Deseja editar outra Ordem de serviço?(s/n)")
    escolhaLoop=input()
    if(escolhaLoop!="s"):
      break 


