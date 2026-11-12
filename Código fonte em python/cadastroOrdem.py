from classes import OrdemDeServico
from singletonOrdem import repoServico

def funcaoCadastroOrdem():
    while True:
        nome    = input("Digite o nome da ordem de serviço: ")
        preco = float(input("Digite o preço da ordem de serviço: "))

        if repoServico.adicionar(OrdemDeServico(nome,preco)):
            print("Cadastro feito com sucesso.")
        else:
            print("Ordem de serviço já cadastrada (ID duplicado).")

        if input("Deseja cadastrar outro serviço? (s/n): ") != "s":
            break

    print("\n==Lista de ordens de serviço cadastradas==")
    for p in repoServico.listar():
        print(p)
    return
