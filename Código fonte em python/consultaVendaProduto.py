from singletonVendasProdutos import repoVendasProdutos
from singletonCliente import repoClientes

def funcaoFiltrarAno(vendas:list,ano_inicial:int,ano_final:int):
    filtradas=[]
    for v in vendas:
        if ano_inicial<=v.data.ano <= ano_final:
            filtradas.append(v)
    for v in filtradas:
        print(v)
    total = 0
    for v in filtradas:
        total+=v.total
    quantidade= 0
    for v in filtradas:
        quantidade+=1
    print(f"Faturamento: R${total}")
    print(f"Quantidade de vendas:{quantidade}")
    print(f"Período:{ano_inicial} -> {ano_final}")

def funcaoFiltrarMes(vendas:list,ano:int,mes_inicial:int,mes_final:int):
    filtradas=[]
    for v in vendas:
        if ano == v.data.ano:
            if mes_inicial<= v.data.mes <=mes_final:
                filtradas.append(v)

    for v in filtradas:
        print(v)
    total = 0
    for v in filtradas:
        total+=v.total
    quantidade= 0
    for v in filtradas:
        quantidade+=1
    print(f"Faturamento: R${total}")
    print(f"Quantidade de vendas:{quantidade}")
    print(f"Período: {mes_inicial}/{ano} -> {mes_final}/{ano}")
    

def funcaoFiltrarDia(vendas:list,ano:int,mes:int,dia_inicial:int,dia_final:int):
    filtradas=[]
    for v in vendas:
        if ano==v.data.ano:
            if mes== v.data.mes:
                if dia_inicial<=v.data.dia<=dia_final:
                    filtradas.append(v)
    for v in filtradas:
        print(v)
    total = 0
    for v in filtradas:
        total+=v.total
    quantidade= 0
    for v in filtradas:
        quantidade+=1
    print(f"Faturamento: R${total}")
    print(f"Quantidade de vendas:{quantidade}")
    print(f"Período:{dia_inicial}/{mes}/{ano} -> {dia_final}/{mes}/{ano}")

def funcaoMelhoresVendasTotal(compradores):
    n=len(compradores)
    for i in range(n):
        for j in range(n-i-1):
            if(compradores[j].total<compradores[j+1].total):
                temp=compradores[j]
                compradores[j]=compradores[j+1]
                compradores[j+1]=temp
    return compradores

def funcaoMelhoresVendasQuantidade(compradores):
    n=len(compradores)
    for i in range(n):
        for j in range(n-i-1):
            if(compradores[j].quantidade<compradores[j+1].quantidade):
                temp=compradores[j]
                compradores[j]=compradores[j+1]
                compradores[j+1]=temp
    return compradores




def funcaoVendaProduto():
        print("Opções de consulta das vendas: ")
        print("1-Consulta geral")
        print("2-Consulta com cliente")
        print("3-Consulta com tempo")
        print("4-Consulta com maior valor total de venda")
        print("5-Consulta com maior quantidade")
        opcao=int(input())
        if(opcao==1):
            for v in repoVendasProdutos.listar():
                print(v)
        elif(opcao==2):
            print("Escolha com base no ID o cliente que deseja consultar: ")
            for c in repoClientes.listar():
                print(c)
            opcaoCliente=int(input())
            clienteSelecionado = repoClientes.buscar_por_id(opcaoCliente)
            if clienteSelecionado is None:           
                print("Cliente não encontrado.")
                return             
            vendas = repoVendasProdutos.buscar_por_cliente(clienteSelecionado)
            if not vendas:
                print("Nenhuma venda encontrada.")
            else:
                for v in vendas:
                    print(v)
        elif(opcao==3):
            print("==Período para relatório==")
            print("1-Ano")
            print("2-Mês")
            print("3-Dia")
            escolha=int(input())
            if(escolha==1):
                print("Digite o ano inicial: ")
                anoInicial=int(input())
                print("Digite o ano final: ")
                anoFinal=int(input())
                funcaoFiltrarAno(repoVendasProdutos.listar(),anoInicial,anoFinal)
            elif(escolha==2):
               print("Digite o ano: ")
               ano=int(input())
               print("Digite o mês inicial: ")
               mesInicial=int(input())
               print("Digite o mês final: ")
               mesFinal=int(input())
               funcaoFiltrarMes(repoVendasProdutos.listar(),ano,mesInicial,mesFinal)
            elif(escolha==3):
                print("Digite o ano: ")
                ano=int(input())
                print("Digite o mês: ")
                mes=int(input())
                print("Digite o dia inicial: ")
                diaInicial=int(input())
                print("Digite o dia final: ")
                diaFinal=int(input())
                funcaoFiltrarDia(repoVendasProdutos.listar(),ano,mes,diaInicial,diaFinal)
        
        elif(opcao==4):
            lista=funcaoMelhoresVendasTotal(repoVendasProdutos.listar())
            for i in lista:
                print(i)
        elif(opcao==5):
            lista2=funcaoMelhoresVendasQuantidade(repoVendasProdutos.listar())
            for i in lista2:
                print(i)
            

