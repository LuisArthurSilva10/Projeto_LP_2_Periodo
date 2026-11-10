import edicaoProduto
import consultaCliente
import consultaOrdem
import consultaVendaProduto
import consultaVendaOrdem

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
             consultaCliente.funcaoConsultaCliente()
          elif(opcaoCadastro==3):
             consultaOrdem.funcaoConsultaOrdem()
          elif(opcaoCadastro==4):
              consultaVendaProduto.funcaoVendaProduto()
          elif(opcaoCadastro==5):
              consultaVendaOrdem.funcaoVendaOrdem()
          elif(opcaoCadastro==0):
             break
          else:
            print("Digite uma opção válida: ")
          
               