
class consultaClientes:
    def __init__(self):
        self.lista=[]
    def listaClientes(self,listaCadastrada):
        self.lista.extend(listaCadastrada)
    def exibicao(self):
        print("==Consulta de todos os clientes cadastrados==")
        if not self.lista:
            print("Nenhum cliente cadastrado")
            return
        for cliente in self.lista:
            print(f"{cliente}")

sistema=consultaClientes()

def funcaoConsultaClientes():
    sistema.exibicao()
    

