class Client():
    identificador = 1

    def __init__(self, nome, sobrenome, cpf, banco):
        self.id = Client.identificador
        Client.identificador += 1
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.banco = banco

    def __str__(self):
        return (f'O id do cliente é: {self.id}\n'
                f'O nome do cliente: {self.nome} {self.sobrenome}\n'
                f'CPF: {self.cpf}\n')
