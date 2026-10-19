from classes import Cliente

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

def funcaoCadastroCliente():
    sistemaClientes=cadastroCliente()
    while True:
        print("Digite o nome do cliente: ")
        nome=input()
        print("Digite o contato do cliente: ")
        contato=input()
        print("Digite o cpf do cliente (caso não tenha digite 0): ")
        cpf=input()

        cliente=Cliente(nome,contato,cpf)

        sistemaClientes.cadastro(cliente)

        print("Deseja cadastrar outro cliente?(s/n): ")
        opcao=input()
        if(opcao!="s"):
            sistemaClientes.exibicao()
            break

print("Saindo da área de cadastro de clientes...")



