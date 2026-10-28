import random

class FilaVaziaError(Exception):
    def __init__(self):
        print('Fila vazia!')

class Fila():
    def __init__(self):
        self.__lista_nomes = []
        self.__lista_senhas = []

    def Senha(self):
        senha = random.randint(1,999)

        if senha in self.__lista_senhas:
            self.Senha()
        else:
            self.__lista_senhas.append(senha)
            return senha
    
    def addFila(self, nome):
        __senha = self.Senha()
        self.__lista_nomes.append([nome,__senha])
    
    def getFila(self):
        fila = self.__lista_nomes
        return fila
    
    def MostraFila(self):
        fila = self.getFila()
        if fila == []:
            raise IndexError

        for e in fila:
            print(f'|{e[0]} {e[1]:03d}| ', end='', flush=True)
        print('\n')
    
    def atender(self):
        if self.__lista_nomes != []:
            nome, senha = self.__lista_nomes.pop(0)
            print(f'''
======== Nome : {nome} ========
======== Senha : {senha:03d} ========
''')
        else:
            raise IndexError

def Menu():
    print('''
Selecione a ação desejada:

1. Retirar uma senha
2. Atender
3. Mostrar fila

0. Sair
''')
    return input('>>> ')

if __name__ == "__main__":
    fila_unica = Fila()

    while True:
        try:
            menu = Menu()
            if menu == '0':
                raise KeyboardInterrupt
            elif menu =='1':
                nome = input('Digite seu nome: ')
                if nome.isnumeric():
                    raise BaseException
                fila_unica.addFila(nome)
                continue
            elif menu == '2':
                fila_unica.atender()
                continue
            elif menu == '3':
                fila_unica.MostraFila()
                continue
            else:
                raise BaseException

        except KeyboardInterrupt:
            print('Programa encerrado!')
            break
        except IndexError:
            FilaVaziaError()
        except:
            print('ERRO: Algo deu errado, tente novamente!')
