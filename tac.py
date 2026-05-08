from itertools import combinations

# magic square mapping
m = {1:8, 2:1, 3:6, 4:3, 5:5, 6:7, 7:4, 8:9, 9:2}

# board
b = [" "] * 10

# moves
x = []
o = []

def show():
    print(b[1],"|",b[2],"|",b[3])
    print("--+--+--")
    print(b[4],"|",b[5],"|",b[6])
    print("--+--+--")
    print(b[7],"|",b[8],"|",b[9])
    print()

def win(mv):
    # check all combinations of 3 moves
    for a, b, c in combinations(mv, 3):
        if a + b + c == 15:
            return True
    return False

def full():
    return all(b[i] != " " for i in range(1, 10))

while True:
    show()

    # X move
    try:
        p = int(input("X move (1-9): "))
        if p < 1 or p > 9:
            print("Invalid position! Try again.")
            continue
        if b[p] != " ":
            print("Position already taken! Try again.")
            continue
    except:
        print("Enter a valid number!")
        continue

    b[p] = "X"
    x.append(m[p])

    if win(x):
        show()
        print(" X wins!")
        break

    if full():
        show()
        print("It's a draw!")
        break

    show()

    # O move
    try:
        p = int(input("O move (1-9): "))
        if p < 1 or p > 9:
            print("Invalid position! Try again.")
            continue
        if b[p] != " ":
            print("Position already taken! Try again.")
            continue
    except:
        print("Enter a valid number!")
        continue

    b[p] = "O"
    o.append(m[p])

    if win(o):
        show()
        print("O wins!")
        break

    if full():
        show()
        print("It's a draw!")
        break