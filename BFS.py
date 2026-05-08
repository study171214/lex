from collections import deque

def next_states(a,b,A,B):
    return [
        (A,b),(a,B),(0,b),(a,0),
        (a-min(a,B-b), b+min(a,B-b)),
        (a+min(b,A-a), b-min(b,A-a))
    ]

def bfs(A,B,T):
    q = deque([((0,0),[(0,0)])])
    v = set()
    while q:
        (a,b),p = q.popleft()
        if a==T or b==T:
            return p
        if (a,b) in v:
            continue
        v.add((a,b))
        for s in next_states(a,b,A,B):
            if s not in v:
                q.append((s,p+[s]))

A = int(input("Jug A: "))
B = int(input("Jug B: "))
T = int(input("Target: "))

res = bfs(A,B,T)

print("BFS Path:")
for i,(a,b) in enumerate(res):
    print(i,":",a,b)