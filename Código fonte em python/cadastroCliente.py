from classes import Cliente
from singletonCliente import repoClientes

def funcaoCadastroCliente():
    while True:
        nome    = input("Digite o nome do cliente: ")
        contato = input("Digite o contato do cliente: ")
        cpf     = input("Digite o cpf do cliente (caso não tenha digite 0): ")

        cliente = Cliente(nome, contato, cpf)

        if repoClientes.adicionar(cliente):
            print("Cadastro feito com sucesso.")
        else:
            print("Cliente já cadastrado (ID ou CPF duplicado).")

        if input("Deseja cadastrar outro cliente? (s/n): ") != "s":
            break

    print("\n==Lista de clientes cadastrados==")
    for c in repoClientes.listar():
        print(c)

    return
