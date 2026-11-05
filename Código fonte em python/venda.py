import vendaProduto
import vendaOrdem

def opcoesVenda():
    print("\n\n==ÁREA DE VENDA==")
    print("1-Produto")
    print("2-Ordem de serviço")
    print("0-Sair")
def vendaUniversal():          
    while True:    
          opcoesVenda()
          opcaoVenda=int(input())
          if(opcaoVenda==1):
            vendaProduto.funcaoVendaProduto()
          elif(opcaoVenda==2):
             vendaOrdem.funcaoVendaOrdem()
          elif(opcaoVenda==0):
             break
          else:
            print("Digite uma opção válida: ")
          
               