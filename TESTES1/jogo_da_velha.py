#jogo da velha
tabela = [[' 7 ', ' 8 ', ' 9 '], [' 4 ', ' 5 ', ' 6 '], [' 1 ', ' 2 ', ' 3 ']]
tabela2 = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]
jogada = ' X '

for x, e in enumerate(tabela):
    print('|'.join(tabela2[x]))

    print('---+---+---') if x < 2 else print()

fim = 0
while fim < 9:
    try:
        lista = tabela[0]

        print('=' * 20)
        
        print(f'vez do jogador {jogada}')
        linha = int(input('\nlinha (1 a 3): '))
        coluna = int(input('coluna (1 a 3): '))

        if linha > 3 or coluna > 3:
            print('\nvalor inválido!\n')
            continue

        elif (tabela[linha - 1][coluna - 1]).strip().isnumeric() == False:
            print('\nvalor ja usado!\n')
            continue

        else:
            if jogada == ' X ':
                tabela[linha - 1][coluna - 1] = jogada
                tabela2[linha - 1][coluna - 1] = jogada
                jogada = ' O '

            elif jogada == ' O ':
                tabela[linha - 1][coluna - 1] = jogada
                tabela2[linha - 1][coluna - 1] = jogada
                jogada = ' X '

            print('=' * 20)
            print()

            for x, e in enumerate(tabela):
                print('|'.join(tabela2[x]))

                print('---+---+---') if x < 2 else print()

            for x, e in enumerate(tabela):
                lista = tabela[0]
            
                if tabela[x][0] == tabela[x][1] and tabela[x][0] == tabela[x][2]:
                    #horizontal
                    print(f'o jogador {''.join(lista[0])} venceu\n')
                    fim = 14
                    break

                elif lista[x] == tabela[1][x] and lista[x] == tabela[2][x]:
                    #vertical
                    print(f'o jogador {''.join(lista[x])} venceu\n')
                    fim = 14
                    break

                elif lista[0] == tabela[1][1] and lista[0] == tabela[2][2]:
                    #diagonal 1:3
                    print(f'o jogador {''.join(lista[0])} venceu\n')
                    fim = 14
                    break

                elif lista[2] == tabela[1][1] and lista[2] == tabela[2][0]:
                    #diagonal 1:1
                    print(f'o jogador {''.join(lista[2])} venceu\n')
                    fim = 14
                    break

            fim += 1
    
    except:
        print('Valor inválido')