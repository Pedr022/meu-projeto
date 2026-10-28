estados = {'mato grosso': ['MT','Sinop', 'Cuiabá'],
           'santa catarina': ['SC', 'Navegantes', 'Balneário Camboriú']}

cidades = {'sinop': ['população: 200.000'],
           'cuiabá': ['população: 600.000']}

class Banco:
    def __init__(self, nome, estado, cidade):
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.estado = estado.lower(), ', '.join(estados[estado.lower()])
        self.cidade = cidade.lower(), ', '.join(cidades[cidade.lower()])

    
    def abre_conta(self, conta):
        self.contas.append(conta)
    
    def lista_contas(self):
        for c in self.contas:
            c.resumo()

teste = Banco('pedro', 'Mato Grosso', 'sinop')
print(f'{teste.estado}\n{teste.cidade}')