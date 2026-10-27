
class consultaProdutos:
    def __init__(self):
        self.lista=[]
    def listaProdutos(self,listaCadastrada):
        self.lista.extend(listaCadastrada)
    def exibicao(self):
        print("==Consulta de todos os produtos cadastrados==")
        if not self.lista:
            print("Nenhum produto cadastrado")
            return
        for produto in self.lista:
            print(f"{produto}")

sistema=consultaProdutos()

def funcaoConsultaProdutos():

    sistema.exibicao()
    

