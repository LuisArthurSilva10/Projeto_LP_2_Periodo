from classes import Produto


class cadastroProdutos:
    
    def __init__ (self):
        self.lista=[]
    def cadastro (self,produto):
        self.lista.append(produto)
        print("Cadastro feito com sucesso!")
    def exibicao (self):
        print("\n\n==Lista dos produtos cadastrados==")
        if not self.lista:
            print("Nenhum produto cadastrado no momento")
            return
        for produto in self.lista:
            print(f"{produto}")

def funcaoCadastroProdutos():
    sistemaProdutos=cadastroProdutos()

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
           sistemaProdutos.exibicao()
           break

print("Saindo da área de cadastro de produtos...\n")
    
