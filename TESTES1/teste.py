L = [15,22,3,9,10,8]

n1 = int(input('digite o número a ser encontrado: '))
n2 = int(input('digite um segundo número a ser encontrado: '))

encontrado1 = False
x = 0

while x < len(L):
    if L[x] == n1:
        encontrado1 = True
        break
    
    x += 1

encontrado2 = False
y = 0

while y < len(L):
    if L[y] == n2:
        encontrado2 = True
        break

    y += 1

if encontrado1 and encontrado2:
    if x < y:
        print(f'Primeiro: {n1} Posição: {x + 1}\nSegundo: {n2} Posição: {y + 1}')

    elif y < x:
        print(f'Primeiro: {n2} Posição: {y + 1}\nSegundo: {n1} Posição: {x + 1}')

    else:
        print(f'o número {n1} foi encontrado na posição {x + 1}')

elif encontrado1:
    print(f'o número {n1} foi encontrado na posição {x + 1}\no número {n2} não foi encontrado')

elif encontrado2:
    print(f'o número {n2} foi encontrado na posição {y + 1}\no número {n1} não foi encontrado')

else:
    print('nenhum número foi encontrado')