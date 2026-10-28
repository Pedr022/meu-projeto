L = [1,7,4,8,10,0,-7]

fim = len(L)

while fim > 1:
    trocado = False

    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp

            trocado = True
        
        x += 1
    
    if not trocado:
        break

    fim -= 1

for e in L:
    print(e, end=', ')