def escreverMatriz(matriz):
    for e in matriz:
        for i in e:
            print(i)
        print('\n')

numeros = '123456789'

linhas = [['','',''] for e in range(3)]
matriz = [linhas for e in range(3)]
conj_matriz = [matriz for e in range(3)]

numero_digitado = int(input('digite 9 números: '))
for x,n in enumerate(numero_digitado):
    conj_matriz[0]

escreverMatriz(conj_matriz)