b = [' ']*9

def show():
    for i in range(0,9,3):
        print(b[i],"|",b[i+1],"|",b[i+2])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(b[x]==b[y]==b[z]==p for x,y,z in w)

def full():
    return ' ' not in b

def minimax(isMax):
    if win('O'): return 1
    if win('X'): return -1
    if full(): return 0

    if isMax:
        best = -999
        for i in range(9):
            if b[i]==' ':
                b[i]='O'
                best = max(best, minimax(False))
                b[i]=' '
        return best
    else:
        best = 999
        for i in range(9):
            if b[i]==' ':
                b[i]='X'
                best = min(best, minimax(True))
                b[i]=' '
        return best

def comp():
    best = -999
    pos = -1
    for i in range(9):
        if b[i]==' ':
            b[i]='O'
            score = minimax(False)
            b[i]=' '
            if score > best:
                best = score
                pos = i
    b[pos]='O'

while True:
    show()
    p = int(input("Move (1-9): ")) - 1
    if b[p]==' ':
        b[p]='X'

    if win('X'):
        show(); print("You win"); break
    if full():
        show(); print("Draw"); break

    comp()

    if win('O'):
        show(); print("Computer wins"); break
    if full():
        show(); print("Draw"); break