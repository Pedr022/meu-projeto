#  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
#  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
#  25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0


def codificador(mensagem):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codificador = 'zyxwvutsrqponmlkjihgfedcba'

    lista_alfabeto = list(alfabeto)
    lista_codificador = list(codificador)
    lista_mensagem = list(mensagem.upper())

    for posicao, letra in enumerate(lista_alfabeto):

        for x, e in enumerate(lista_mensagem):
            if letra == e:
                lista_mensagem[x] = lista_codificador[posicao]

    return ''.join(lista_mensagem)

def decodificador(mensagem):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codificador = 'zyxwvutsrqponmlkjihgfedcba'

    lista_alfabeto = list(alfabeto)
    lista_codificador = list(codificador.upper())
    lista_mensagem = list(mensagem.upper())

    for posicao, letra in enumerate(lista_codificador):

        for x, e in enumerate(lista_mensagem):
            if letra == e:
                lista_mensagem[x] = (lista_alfabeto[posicao]).lower()

    return ''.join(lista_mensagem)

print(codificador(input('Digite um texto: ')))
print(decodificador(input('Digite o texto codificado: ')))
