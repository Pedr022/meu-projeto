class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.saldo = 0
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    
    def resumo(self):
        print(f'{'='*30}\n')
        for x, e in enumerate((self.clientes)):
            print(f'nome {x + 1}: {e.nome} telefone: {e.telefone}')
        print(f'\nNúmero da conta: {self.numero} saldo: {self.saldo:.2f}\n')
        print(f'{'='*30}\n')
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        
        else:
            print('Saldo insuficiente!')
            return False
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'Extrato CC N {self.numero}\n')

        for o in self.operacoes:
            print(f'{o[0]} {o[1]}')
        print(f'\n    Saldo: {self.saldo:.2f}\n')


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite
    
    def extrato(self):
        print(f'Extrato CC N {self.numero}\n')

        for o in self.operacoes:
            print(f'{o[0]} {o[1]}')
        
        
        print(f'''
    Saldo: {self.saldo:.2f}
    Limite: {self.limite}
    Saque disponível: {self.saldo + self.limite}
''')
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        
        else:
            return False
        