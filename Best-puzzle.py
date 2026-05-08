import heapq

goal = []

print("Enter the 3x3 goal state row by row:")

for i in range(3):
    goal.append(list(map(int, input().split())))

def h(s):

    count = 0

    for i in range(3):
        for j in range(3):

            if s[i][j] != 0 and s[i][j] != goal[i][j]:
                count += 1

    return count

def find0(s):

    for i in range(3):
        for j in range(3):

            if s[i][j] == 0:
                return i, j

def next_states(s):

    r, c = find0(s)

    moves = [
        (r-1,c),
        (r+1,c),
        (r,c-1),
        (r,c+1)
    ]

    res = []

    for nr, nc in moves:

        if 0 <= nr < 3 and 0 <= nc < 3:

            ns = [row[:] for row in s]

            ns[r][c], ns[nr][nc] = ns[nr][nc], ns[r][c]

            res.append(ns)

    return res

def best_first(start):

    pq = [(h(start),start,[])]

    visited = set()

    while pq:

        hval,cur,path = heapq.heappop(pq)

        if cur == goal:
            return path + [(cur,hval)]

        if str(cur) in visited:
            continue

        visited.add(str(cur))

        for ns in next_states(cur):

            heapq.heappush(
                pq,
                (h(ns),ns,path + [(cur,hval)])
            )

print("Enter puzzle:")

start = [list(map(int,input().split())) for _ in range(3)]

res = best_first(start)

print("\nSteps:\n")

for st,hval in res:

    print("h(n) =", hval)

    for r in st:
        print(r)

    print()
