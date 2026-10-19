from classes import OrdemDeServico

class cadastroOrdem:
    def __init__(self):
        self.listaOrdem=[]
    def cadastro(self,Ordem):
        self.listaOrdem.append(Ordem)
        print("\nCadastro feito com sucesso!")
    def exibicao(self):
        print("\n\n==Lista de Ordens de serviço cadastradas==")
        if not(self.listaOrdem):
            print("Nenhuma Ordem de serviço cadastrada.")
            return
        for ordem in self.listaOrdem:
            print(f"{ordem}")

def funcaoCadastroOrdem():
    sistemaOrdem=cadastroOrdem()
    while True:
        print("Digite o nome da ordem de serviço: ")
        nome= input()
        print("Digite o preço da ordem de serviço: ")
        preco=float(input())

        ordemCadastrada=OrdemDeServico(nome,preco)
        sistemaOrdem.cadastro(ordemCadastrada)

        print("Deseja cadastrar outra Ordem de Serviço(s/n): ")
        opcao=input().lower()
        if(opcao!="s"):
            sistemaOrdem.exibicao()
            break
print("Saindo da área de cadastro de Ordem de serviço...")

