from collections import deque

def next_states(a, b, c, A, B, C):
    states = []

    # Fill operations
    states.append((A, b, c))
    states.append((a, B, c))
    states.append((a, b, C))

    # Empty operations
    states.append((0, b, c))
    states.append((a, 0, c))
    states.append((a, b, 0))

    # Pour A -> B
    t = min(a, B - b)
    states.append((a - t, b + t, c))

    # Pour A -> C
    t = min(a, C - c)
    states.append((a - t, b, c + t))

    # Pour B -> A
    t = min(b, A - a)
    states.append((a + t, b - t, c))

    # Pour B -> C
    t = min(b, C - c)
    states.append((a, b - t, c + t))

    # Pour C -> A
    t = min(c, A - a)
    states.append((a + t, b, c - t))

    # Pour C -> B
    t = min(c, B - b)
    states.append((a, b + t, c - t))

    return states


def bfs(A, B, C, T):
    q = deque([((0, 0, 0), [(0, 0, 0)])])
    visited = set()

    while q:
        (a, b, c), path = q.popleft()

        # Target found
        if a == T or b == T or c == T:
            return path

        if (a, b, c) in visited:
            continue

        visited.add((a, b, c))

        for state in next_states(a, b, c, A, B, C):
            if state not in visited:
                q.append((state, path + [state]))


# Input
A = int(input("Capacity of Jug A: "))
B = int(input("Capacity of Jug B: "))
C = int(input("Capacity of Jug C: "))
T = int(input("Target: "))

# BFS Search
res = bfs(A, B, C, T)

# Output
if res:
    print("\nBFS Path:")
    for i, (a, b, c) in enumerate(res):
        print(i, ":", a, b, c)
else:
    print("No solution found")