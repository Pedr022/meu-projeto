fila = 10
L = list(range(1, (fila + 1)))

while True:
    print('Para ser atendido aperte A')
    print('Para entrar na fila aperte F')
    print('Para sair digite S')
    print(f'existem {len(L)} clientes na fila')
    operacao = input('Digite sua operação:')

    if operacao == 'A':
        if (len(L)) > 0:
            atendido = L.pop(0)
            print(f'Cliente {atendido}')
        
        else:
            print('Fila vazia!')
    
    elif operacao == 'F':
        fila += 1
        L.append(fila)

    elif operacao == 'S':
        break

    else:
        print('Operação inválida! Digite apenas A, F ou S!')
