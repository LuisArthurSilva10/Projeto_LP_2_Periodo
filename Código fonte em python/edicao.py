import edicaoProduto
import edicaoCliente
import edicaoOrdem
import edicaoVendasProdutos
import edicaoVendasOrdem

def opcoesConsulta():
    print("\n\n==ÁREA DE EDIÇÃO==")
    print("1-Produto")
    print("2-Cliente")
    print("3-Ordem de serviço")
    print("4-Venda de produto")
    print("5-Venda de ordem de serviço")
    print("0-Sair")

def edicaoUniversal():
    while True:
          opcoesConsulta()          
          opcaoCadastro=int(input())
          if(opcaoCadastro==1):
             edicaoProduto.funcaoEdicaoProduto()
          elif(opcaoCadastro==2):
             edicaoCliente.funcaoEdicaoCliente()
          elif(opcaoCadastro==3):
             edicaoOrdem.funcaoEdicaoOrdem()
          elif(opcaoCadastro==4):
              edicaoVendasProdutos.funcaoEdicaoVendasProdutos()
          elif(opcaoCadastro==5):
               edicaoVendasOrdem.funcaoEdicaoVendasOrdem()
          elif(opcaoCadastro==0):
             break
          else:
            print("Digite uma opção válida: ")
          
               