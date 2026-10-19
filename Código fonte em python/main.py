
import cadastro

def exibirOpcoes():
    print("\n\n--Sistema para Assistência Técnica--")
    print("1-Cadastro")
    print("2-Consulta")
    print("3-Vender")
    print("0-Sair")



while True:
    exibirOpcoes()
    opcaoInicial=int(input())

    if(opcaoInicial==1):
         cadastro.cadastroUniversal()
    
    elif(opcaoInicial==2):
        print("Consulta")
    
    
    elif(opcaoInicial==3):
        print("Venda")
        
    elif(opcaoInicial==0):
        break
    else:
        print("Digite um número válido.")

print("Até mais")
