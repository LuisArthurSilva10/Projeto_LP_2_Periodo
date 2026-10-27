from classes import OrdemDeServico
from consultaOrdem import sistema

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
    def commit(self):
        sistema.lista.clear()
        sistema.lista.extend(self.listaOrdem)
        

sistemaOrdem=cadastroOrdem()

def funcaoCadastroOrdem():
  
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
            break
        
    sistemaOrdem.exibicao()
    sistemaOrdem.commit()


