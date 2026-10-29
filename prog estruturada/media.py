def getNotas():
    return float(input('Digite sua nota: '))

def calcMedia(lista):
    return sum(lista) / len(lista)

def verifMedia(valor, media=6):
    if valor >= media:
        return 'Aprovado', media
    elif valor >= (media-2):
        return 'Recuperação', media
    else:
        return 'Reprovado', media

def escreveStatus(media, aprovacao, media_necessaria):
    print(f'''
    Status do aluno: {aprovacao}
    Média: {media:.2f}
    Média necessária: {media_necessaria}
    ''')
    return

def Menu():
    print('''
Escolha uma ação:
1. Calcular média
0. Sair
''')
    return int(input('>>> '))

lista_notas = []

while True:
    try:
        menu = Menu()

        if menu == 0:
            raise KeyboardInterrupt
        
        for e in range(3):
            lista_notas.append(getNotas())

        media = calcMedia(lista_notas)
        verif_aprovacao, media_necessaria = verifMedia(media, 5)

        escreveStatus(media, verif_aprovacao, media_necessaria)
        break

    except KeyboardInterrupt:
        print('Programa encerrado')
        break
    except:
        print('Ops, algo deu errado, tente novamente!')
