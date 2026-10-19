import cadastroProduto
import cadastroCliente
import cadastroOrdem

def opcoesCadastro():
    print("\n\n==ÁREA DE CADASTRO==")
    print("1-Produto")
    print("2-Cliente")
    print("3-Ordem de serviço")
    print("0-Sair")

def cadastroUniversal():
    while True:
          opcoesCadastro()          
          opcaoCadastro=int(input())
          if(opcaoCadastro==1):
             cadastroProduto.funcaoCadastroProdutos()
          
          elif(opcaoCadastro==2):
             cadastroCliente.funcaoCadastroCliente()
          
          elif(opcaoCadastro==3):
             cadastroOrdem.funcaoCadastroOrdem()
          elif(opcaoCadastro==0):
             break
          else:
            print("Digite uma opção válida: ")
          
               