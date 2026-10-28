#jogo da forca
a = 'palavra, cachorro, capoeira, dançarino, pedaleira, estrela, cachoeira, macaco, praieiro, acerola, carroça, caminhoneiro'
lista_de_palavras = list(a.split(','))
numero = int(input('digite um número: '))
indice = (numero * 776) % len(lista_de_palavras)

palavra = lista_de_palavras[indice].strip()
for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

linha1 = list('X  0  ')
linha2 = list('X     ')
linha3 = list('X     ')
linha4 = list('=' * (len(lista_de_palavras[indice]) - 1))

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    print(' '.join(digitadas))
    print(''.join(linha4))

    if senha == palavra:
        print('você acertou!')
        break

    tentativa = input('\ndigite uma letra: ').lower().strip()

    if tentativa in digitadas:
        print('você ja tentou esta letra!')
        continue

    else:
        digitadas += tentativa

        if tentativa in palavra:
            acertos += tentativa

        else:
            erros += 1
            print('você errou!')

        print('X==:==\nX  :  ')
        print(''.join(linha1) if erros >= 1 else 'X')

        if erros == 2:
            linha2[3] = '|'

        elif erros == 3:
            linha2[2] = '/'

        elif erros >= 4:
            linha2[4] = '\\'

        print(''.join(linha2))

        if erros == 5:
            linha3[2] = '/'

        elif erros >= 6:
            linha3[4] = '\\'

        print(''.join(linha3))
        print('X\n===========')

        if erros == 6:
            print('enforcado!')
            print(f'a palavra era: {palavra}\n')
            break