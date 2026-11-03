import vendaProduto

def opcoesVenda():
    print("\n\n==ÁREA DE VENDA==")
    print("1-Produto")
    print("2-Ordem de serviço")
    print("0-Sair")

def vendaUniversal():
    opcoesVenda()          
    while True:    
          opcaoVenda=int(input())
          if(opcaoVenda==1):
            vendaProduto.funcaoVendaProduto()
          elif(opcaoVenda==2):
             print("Venda Ordem")
          elif(opcaoVenda==0):
             break
          else:
            print("Digite uma opção válida: ")
          
               