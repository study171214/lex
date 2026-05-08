import heapq, math

def h(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def best_first(g, s, goal):
    r,c = len(g), len(g[0])
    heap = [(h(s,goal), s, [s])]
    v = set([s])

    while heap:
        _,cur,path = heapq.heappop(heap)

        if cur == goal:
            return path

        x,y = cur
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and g[nx][ny]==0 and (nx,ny) not in v:
                v.add((nx,ny))
                heapq.heappush(heap,(h((nx,ny),goal),(nx,ny),path+[(nx,ny)]))

def show(g, path, s, goal):
    p = set(path)
    for i in range(len(g)):
        for j in range(len(g[0])):
            if (i,j)==s: print("S",end=" ")
            elif (i,j)==goal: print("G",end=" ")
            elif g[i][j]==1: print("#",end=" ")
            elif (i,j) in p: print(".",end=" ")
            else: print("_",end=" ")
        print()

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# input
r = int(input("Rows: "))
c = int(input("Cols: "))

g = [list(map(int,input().split())) for _ in range(r)]

sx,sy = map(int,input("Start: ").split())
gx,gy = map(int,input("Goal: ").split())

s = (sx-1, sy-1)

goal = (gx-1, gy-1)

path = best_first(g,(sx,sy),(gx,gy))

print("\nPath:")
print(path)

print("\nGrid:")
show(g,path,(sx,sy),(gx,gy))
print("Euclidean Distance =", h((sx,sy),(gx,gy)))
print("Manhattan Distance =", manhattan((sx,sy),(gx,gy)))

# rows =4
# cols =4

# 0 0 0 0
# 1 1 0 1
# 0 0 0 0
# 0 1 1 0

# start = 0 0
# goal = 3 3