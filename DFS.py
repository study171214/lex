def next_states(a,b,A,B):
    return [
        (A,b),(a,B),(0,b),(a,0),
        (a-min(a,B-b), b+min(a,B-b)),
        (a+min(b,A-a), b-min(b,A-a))
    ]

def dfs(A,B,T):
    st = [((0,0),[(0,0)])]
    v = set()
    while st:
        (a,b),p = st.pop()
        if a==T or b==T:
            return p
        if (a,b) in v:
            continue
        v.add((a,b))
        for s in next_states(a,b,A,B):
            if s not in v:
                st.append((s,p+[s]))

A = int(input("Jug A: "))
B = int(input("Jug B: "))
T = int(input("Target: "))

res = dfs(A,B,T)

print("DFS Path:")
for i,(a,b) in enumerate(res):
    print(i,":",a,b)