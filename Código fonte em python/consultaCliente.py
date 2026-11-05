from singletonCliente import repoClientes
def funcaoConsultaCliente():
   clientes = repoClientes.listar()
   if not clientes:
      print("Nenhum cliente cadastrado.")
      return
   else:
      for cliente in clientes:
         print(cliente)
