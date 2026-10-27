from classes import Produto
from consultaProduto import sistema



class cadastroProdutos:
    
    def __init__ (self):
        self.listaProdutos=[]
    def cadastro (self,produto):
        self.listaProdutos.append(produto)
        print("Cadastro feito com sucesso!")
    def exibicao (self):
        print("\n\n==Lista dos produtos cadastrados==")
        if not self.listaProdutos:
            print("Nenhum produto cadastrado no momento")
            return
        for produto in self.listaProdutos:
            print(f"{produto}")
    def commit(self ):
        sistema.lista.clear()
        sistema.lista.extend(self.listaProdutos)

       

sistemaProdutos=cadastroProdutos()

def funcaoCadastroProdutos():
   

    while True:
       print(f"\nDigite o nome do produto: ")
       nome = input()
       print(f"Digite o preço do produto {nome}: ")
       preco = float(input())
       print(f"Digite a quantidade de unidades disponíveis do produto {nome}")
       quantidade = int(input())

       produtoCadastrado=Produto(nome,preco,quantidade)
       sistemaProdutos.cadastro(produtoCadastrado)
      
       print("Deseja cadastrar outro produto?(s/n)")
       opcao=input().lower()
       if(opcao!="s"):
           break
       
    sistemaProdutos.exibicao()
    sistemaProdutos.commit()

    
