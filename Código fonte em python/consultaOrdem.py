
class consultaOrdem:
    def __init__(self):
        self.lista=[]
    def listaOrdens(self,listaCadastrada):
        self.lista.extend(listaCadastrada)
    def exibicao(self):
        print("==Consulta de todas as ordens de serviço cadastradas==")
        if not self.lista:
            print("Nenhuma ordem de serviço cadastrado")
            return
        for ordem in self.lista:
            print(f"{ordem}")

sistema=consultaOrdem()

def funcaoConsultaOrdem():
    sistema.exibicao()
    

