from datetime import datetime


class Historic():
    def __init_(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprimir_transacoes(self):
        print(f"A data de abertura é: {self.data_abertura}")
        print("== TRANSAÇOES ==")
        for t in self.transacoes:
            print('-', t)
