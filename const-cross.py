def canH(g,w,r,c):
    if c+len(w)>len(g): return False
    for i in range(len(w)):
        if g[r][c+i] not in ('-',w[i]): return False
    return True

def placeH(g,w,r,c):
    t=[]
    for i in range(len(w)):
        t.append(g[r][c+i])
        g[r][c+i]=w[i]
    return t

def undoH(g,t,r,c):
    for i in range(len(t)):
        g[r][c+i]=t[i]

def canV(g,w,r,c):
    if r+len(w)>len(g): return False
    for i in range(len(w)):
        if g[r+i][c] not in ('-',w[i]): return False
    return True

def placeV(g,w,r,c):
    t=[]
    for i in range(len(w)):
        t.append(g[r+i][c])
        g[r+i][c]=w[i]
    return t

def undoV(g,t,r,c):
    for i in range(len(t)):
        g[r+i][c]=t[i]

def solve(g,w,idx):
    if idx==len(w): return True
    word=w[idx]

    for i in range(len(g)):
        for j in range(len(g)):
            if canH(g,word,i,j):
                t=placeH(g,word,i,j)
                if solve(g,w,idx+1): return True
                undoH(g,t,i,j)

            if canV(g,word,i,j):
                t=placeV(g,word,i,j)
                if solve(g,w,idx+1): return True
                undoV(g,t,i,j)
    return False

# input
n=int(input("Size: "))
print("Grid:(-)(+)")
g=[list(input()) for _ in range(n)]
w=input("Words seperated by ',' : ").split(',')

if solve(g,w,0):
    print("\nSolution:")
    for r in g: print(''.join(r))
else:
    print("No solution")

#     Size: 10
# +-++++++++
# +-++++++++
# +-++++++++
# +-----+++
# +-----+++
# +-----+++
# +-++++++++
# +-++++++++
# +-++++++++
# +-++++++++
# Words: LONDON