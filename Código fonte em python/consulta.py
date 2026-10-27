import consultaProduto
import consultaCliente
import cadastroOrdem

def opcoesConsulta():
    print("\n\n==ÁREA DE CONSULTA==")
    print("1-Produto")
    print("2-Cliente")
    print("3-Ordem de serviço")
    print("0-Sair")

def consultaUniversal():
    while True:
          opcoesConsulta()          
          opcaoCadastro=int(input())
          if(opcaoCadastro==1):
             consultaProduto.funcaoConsultaProdutos()
          
          elif(opcaoCadastro==2):
             consultaCliente.funcaoConsultaClientes()
          
          elif(opcaoCadastro==3):
             cadastroOrdem.funcaoCadastroOrdem()
          elif(opcaoCadastro==0):
             break
          else:
            print("Digite uma opção válida: ")
          
               