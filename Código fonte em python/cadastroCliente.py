from classes import Cliente
from classes import ClientesIndexados
from consultaCliente import sistemaConsultaCliente

class cadastroCliente:
    def __init__(self):
        self.listaClientes=[]
    def cadastro(self,cliente):
        self.listaClientes.append(cliente)
        print("\nCadastro feito com sucesso\n")
    def exibicao(self):
        print("\n\n==Lista de clientes cadastrados==")
        if not self.listaClientes:
            print("Nenhum cliente cadastrado")
            return
        for cliente in self.listaClientes:
            print(f"{cliente}")
    def commit(self):
      sistemaConsultaCliente.lista.extend(self.listaClientes)

sistemaClientes=cadastroCliente()
sistemaClientesIndexados=ClientesIndexados()

def funcaoCadastroCliente():
   
    while True:
        print("Digite o nome do cliente: ")
        nome=input()
        print("Digite o contato do cliente: ")
        contato=input()
        print("Digite o cpf do cliente (caso não tenha digite 0): ")
        cpf=input()

        cliente=Cliente(nome,contato,cpf)
        sistemaClientesIndexados.adicionar(cliente)
        sistemaClientes.cadastro(cliente)

        print("Deseja cadastrar outro cliente?(s/n): ")
        opcao=input()
        if(opcao!="s"):
          break
    sistemaClientes.exibicao()
    sistemaClientes.commit()
    



