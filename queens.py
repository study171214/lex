
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
queens = int(input("Enter number of queens: "))

board = [[0 for _ in range(cols)] for _ in range(rows)]
count = 0

# Function to check whether queen placement is safe
def is_safe(r, c):

    # Check upper column
    for i in range(r):
        if board[i][c] == 1:
            return False

    # Check upper-left diagonal
    i, j = r - 1, c - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = r - 1, c + 1
    while i >= 0 and j < cols:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve(row, placed):

    global count

    # Required number of queens placed
    if placed == queens:
        count += 1

        print(f"\nSolution {count}")

        for r in board:
            print(r)

        return

    # If rows finished
    if row >= rows:
        return

    # Try placing queen in every column
    for col in range(cols):

        if is_safe(row, col):

            board[row][col] = 1

            solve(row + 1, placed + 1)

            # Backtrack
            board[row][col] = 0

    # Also allow skipping a row
    solve(row + 1, placed)


# Start solving
solve(0, 0)

print("\nTotal solutions:", count)