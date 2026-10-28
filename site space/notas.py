print('*DIGITE OS NÚMEROS AO LADO*')
print('o que você quer saber?\n1. Média anual\n2. Quanto preciso para passar de ano')

answer = int(input('digite aqui:'))

if answer == 1:

    contador = int(input('quantas matérias são:'))
    tipo = input('o sistema anual da sua ecola é trimestral ou bimestral?(B/T):')

    if tipo == 'T' or tipo == 't':

        peso = input('os trimestres da sua escola tem algum peso?(S/N):')
        if peso == 'S' or peso == 's':

            p1 = float(input('peso 1:'))
            p2 = float(input('peso 2:'))
            p3 = float(input('peso 3:'))
            
            for i in range(0, contador):

                m1 = float(input('média 1:'))
                m2 = float(input('média 2:'))
                m3 = float(input('média 3:'))
                PS = p1 + p2 + p3
                MT = ((m1 * p1) + (m2 * p2) + (m3 * p3)) / PS

                print(f'sua média anual é:{MT:.2f}')
        
        else:

            for i in range(0, contador):
                M1 = float(input('média 1:'))
                M2 = float(input('média 2:'))
                M3 = float(input('média 3:'))
                MT = (M1 + M2 + M3) / 3

                print(f'sua média anual é:{MT:.2f}')

    else:
        peso = input('os bimestres da sua escola tem algum peso?(S/N):')
        if peso == 'S' or peso == 's':

            pe1 = float(input('peso 1:'))
            pe2 = float(input('peso 2:'))
            pe3 = float(input('peso 3:'))
            pe4 = float(input('peso 4:'))

            for i in range(0, contador):

                B1 = float(input('média 1:'))
                B2 = float(input('média 2:'))
                B3 = float(input('média 3:'))
                B4 = float(input('média 4:'))
                ps2 = pe1 + pe2 + pe3 + pe4
                BT = ((B1 * pe1) + (B2 * pe2) + (B3 * pe3) + (B4 * pe4)) / ps2

                print(f'sua média anual é:{BT:.2f}')
        
        else:

            for i in range (0, contador):

                b1 = float(input('média 1:'))
                b2 = float(input('média 2:'))
                b3 = float(input('média 3:'))
                b4 = float(input('média 4:'))
                
                BT = (b1 + b2 + b3 + b4) / 4

                print(f'sua média anual é:{BT:.2f}')

elif answer == 2:

    contador = int(input('quantas matérias são:'))
    tipo = input('o sistema anual da sua ecola é trimestral ou bimestral?(B/T):')

    if tipo == 'T' or tipo == 't':

        print('em qual trimestre você está?\n1. primeiro trimestre\n2. segundo trimestre\n3. terceiro trimestre')
        trimestre = int(input('responda aqui:'))

        if trimestre == 1:

            for i in range(0, contador):

                média = float(input('média da sua escola:'))
                print(f'você tem que tirar mais de {média} nos 3 trimestres para passar')

        elif trimestre == 2:

            média = float(input('média da sua escola:'))
            peso = input('os trimestres da sua escola tem algum peso?(S/N)')

            if peso == 'S' or peso == 's':

                P1 = float(input('peso 1:'))
                P2 = float(input('peso 2:'))
                P3 = float(input('peso 3:'))
                Ps = P1 + P2 + P3

                for i in range(0, contador):

                    M1 = float(input('média do primeiro trimestre:'))

                    MT = ((Ps * média) - (M1 * P1)) / (P2 + P3)

                    print(f'você precisa tirar acima de {MT:.2f} nos próximos dois trimestres para passar')

            else:

                for i in range(0, contador):

                    M1 = float(input('média do primeiro trimestre:'))

                    MT = ((média * 3) - M1) / 2
                    print(f'você precisa tirar acima de {MT:.2f} nos próximos dois trimestres para passar')

        else:

            média = float(input('média da sua escola:'))
            peso = input('os trimestres da sua escola tem algum peso?(S/N)')

            if peso == 'S' or peso == 's':

                P1 = float(input('peso 1:'))
                P2 = float(input('peso 2:'))
                P3 = float(input('peso 3:'))
                Ps = P1 + P2 + P3

                for i in range(0, contador):

                    M1 = float(input('média do primeiro trimestre:'))
                    M2 = float(input('média do segundo trimestre:'))

                    MT = ((média * Ps) - (M1 * P1) - (M2 * P2)) / P3

                    print(f'você precisa tirar acima de {MT:.2f} no próximo trimestre para passar')

            else:

                for i in range(0, contador):

                    M1 = float(input('média do primeiro trimestre:'))
                    M2 = float(input('média do segundo trimestre:'))

                    MT = (3 * média) - M1 - M2

                    print(f'você precisa tirar acima de {MT:.2f} no próximo trimestre para passar')

    else:

        print('em qual bimestres você está?\n1. peimeiro bimestre\n2. segundo bimestre\n3. terceiro bimestre\n4. quarto bimestre')
        bimestre = input('responda aqui:')

        if bimestre == 1:

            for i in range(0, contador):

                média = float(input('média da sua escola:'))

                print(f'você precisa tirar mais de {média} para passar')

        elif bimestre == 2:

            média = float(input('média da sua escola:'))
            peso = input('os bimestres da sua escola tem algum peso?(S/N)')

            if peso == 'S' or peso == 's':

                P1 = float(input('peso 1:'))
                P2 = float(input('peso 2:'))
                P3 = float(input('peso 3:'))
                P4 = float(input('peso 4:'))
                ps = P1 + P2 + P3 + P4
                
                for i in range(0, contador):
                    
                    M1 = float(input('média do primeiro bimestre:'))
                    MT = ((ps * média) - (M1 * P1)) / (P2 + P3 + P4)

                    print(f'você precisa tirar mais de {MT:.2f} para passar')
            
            else:

                for i in range(0, contador):

                    M1 = float(input('média do primeiro bimestre:'))
                    MT = ((4 * média) - M1) / 3

                    print(f'você precisa tirar mais de {MT:.2f} para passar')
        
        elif bimestre == 3:

            média = float(input('média da sua escola:'))
            peso = input('os bimestres da sua escola tem algum peso?(S/N)')

            if peso == 'S' or peso == 's':

                P1 = float(input('peso 1:'))
                P2 = float(input('peso 2:'))
                P3 = float(input('peso 3:'))
                P4 = float(input('peso 4:'))
                ps = P1 + P2 + P3 + P4

                for i in range(0, contador):

                    M1 = float(input('média do primeiro bimestre:'))
                    M2 = float(input('média do segundo bimestre:'))
                    MT = ((ps * média) - (M1 * P1) - (M2 * P2)) / (P3 + P4)

                    print(f'você precisa tirar mais de {MT:.2f} para passar')

            else:

                for i in range(0, contador):

                    M1 = float(input('média do primeiro bimestre:'))
                    M2 = float(input('média do segundo bimestre:'))
                    MT = ((4 * média) - M1 - M2) / 2

                    print(f'você precisa tirar mais de {MT:.2f} para passar')

        else:

            média = float(input('média da sua escola:'))
            peso = input('os bimestres da sua escola tem algum peso?(S/N)')

            if peso == 'S' or peso == 's':

                P1 = float(input('peso 1:'))
                P2 = float(input('peso 2:'))
                P3 = float(input('peso 3:'))
                P4 = float(input('peso 4:'))
                ps = P1 + P2 + P3 + P4

                for i in range(0, contador):

                    M1 = float(input('média do primeiro bimestre:'))
                    M2 = float(input('média do segundo bimestre:'))
                    M3 = float(input('média do terceiro bimestre:'))
                    MT = ((ps * média) - (M1 * P1) - (M2 * P2) - (M3 * P3)) / P4

                    print(f'você precisa tirar mais de {MT:.2f} para passar')

            else:

                for i in range(0, contador):

                    M1 = float(input('média do primeiro bimestre:'))
                    M2 = float(input('média do segundo bimestre:'))
                    M3 = float(input('média do terceiro bimestre:'))
                    MT = (4 * média) - M1 - M2 - M3

                    print(f'você precisa tirar mais de {MT:.2f} par passar')