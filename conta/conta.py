from historic.historic import Historic


class Conta():
    def __init__(self, numero, cliente, saldo):
        self.agencia = cliente.banco.agencia
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.historico = Historic()

    def saque(self, valor):
        if self.saldo < valor:
            print('SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de: {valor} ')
            self.historico.transacoes.append(f'Saque de: {valor}\n'
                                             f' e o saldo de:{self.saldo}')
   
    def deposito(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Deposito de: R$ {valor}\n'
                                         f'e o saldo: {self.saldo}')

    def transferir(self, valor, destino):
        self.saldo -= valor
        destino.saldo += valor
        return(f'O valor transferido foi de: {valor} \n'
               f'O número da conta de destino foi: {destino.numero}')
    
    def extrato(self):
        print(f'O titular da conta é: {self.titular} \n'
              f'Número da conta: {self.numero} \n'
              f'Com o saldo atual de: {self.saldo}')