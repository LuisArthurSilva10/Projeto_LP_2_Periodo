from singletonOrdem import repoServico

if not repoServico.listar():
    print("Nenhuma ordem de serviço cadastrada")
else:
    for servico in repoServico.listar():
        print(servico)
