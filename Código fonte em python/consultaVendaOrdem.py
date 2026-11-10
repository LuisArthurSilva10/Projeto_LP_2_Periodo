from singletonVendasOrdem import repoVendasServico
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


def funcaoVendaOrdem():
        print("Opções de consulta das vendas: ")
        print("1-Consulta geral")
        print("2-Consulta com cliente")
        print("3-Consulta com tempo")
        opcao=int(input())
        if(opcao==1):
            for v in repoVendasServico.listar():
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
            vendas = repoVendasServico.buscar_por_cliente(clienteSelecionado)
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
                funcaoFiltrarAno(repoVendasServico.listar(),anoInicial,anoFinal)
            elif(escolha==2):
               print("Digite o ano: ")
               ano=int(input())
               print("Digite o mês inicial: ")
               mesInicial=int(input())
               print("Digite o mês final: ")
               mesFinal=int(input())
               funcaoFiltrarMes(repoVendasServico.listar(),ano,mesInicial,mesFinal)
            elif(escolha==3):
                print("Digite o ano: ")
                ano=int(input())
                print("Digite o mês: ")
                mes=int(input())
                print("Digite o dia inicial: ")
                diaInicial=int(input())
                print("Digite o dia final: ")
                diaFinal=int(input())
                funcaoFiltrarDia(repoVendasServico.listar(),ano,mes,diaInicial,diaFinal)

            

