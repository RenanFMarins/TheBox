from conta.conta import Conta
from clients.client import Client
from banco.banco import Banco

if '_name_' == '_main_':
    banco1 = Banco('UniBank', 'Rua General Castro 171', '1234')
    cliente1 = Client('Fabricio', 'Dias', '154456987-09', banco1)
    conta1 = Conta('1234', cliente1, 50)
    cliente2 = Client('João', 'Victor', '000123321-45', banco1)
    conta2 = Conta('2345', cliente2, 100)

    print(conta1.transferir(40, conta2))
    print(conta2.saldo)
    print('=================')
    conta1.saque(10)
    conta1.deposito(20)
    conta1.historico.imprime_transacoes()
    print("==================")
    print(conta1.titular)
    print('===================')
    print("Banco")

    banco1.adicionar_clientes(cliente1)
    banco1.adicionar_clientes(cliente2)
    banco1.listar_cliente()
    print("="*10)
    print(cliente2.banco.agencia)