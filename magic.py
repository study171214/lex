n = int(input("Enter odd size: "))
if n % 2 == 0:
    print("Enter odd number only")
    exit()

m = [[0]*n for _ in range(n)]

i = 0
j = n//2

for num in range(1, n*n+1):
    m[i][j] = num

    ni = (i-1) % n
    nj = (j+1) % n

    if m[ni][nj] == 0:
        i, j = ni, nj
    else:
        i = (i+1) % n

for r in m:
    print(r)