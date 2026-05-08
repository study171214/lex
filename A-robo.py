import heapq

def h(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(g, s, goal):
    r,c = len(g), len(g[0])
    pq = [(0,s)]
    cost = {s:0}
    parent = {}

    while pq:
        _,cur = heapq.heappop(pq)

        if cur == goal:
            break

        x,y = cur
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx, y+dy

            if 0<=nx<r and 0<=ny<c and g[nx][ny]==0:
                new = cost[cur] + 1

                if (nx,ny) not in cost or new < cost[(nx,ny)]:
                    cost[(nx,ny)] = new
                    f = new + h((nx,ny),goal)
                    heapq.heappush(pq,(f,(nx,ny)))
                    parent[(nx,ny)] = cur

    # path
    path=[]
    cur=goal
    while cur!=s:
        path.append(cur)
        cur = parent.get(cur)
        if cur is None:
            return None
    path.append(s)
    path.reverse()
    return path

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

# input
r = int(input("Rows: "))
c = int(input("Cols: "))

g = [list(map(int,input().split())) for _ in range(r)]

sx,sy = map(int,input("Start: ").split())
gx,gy = map(int,input("Goal: ").split())
s = (sx-1, sy-1)

goal = (gx-1, gy-1)

path = astar(g,s,goal)

print("\nPath:", path)
print("\nGrid:\n")
show(g,path,s,goal)

# rows =4
# cols =4

# 0 0 0 0
# 1 1 0 1
# 0 0 0 0
# 0 1 1 0

# start = 0 0
# goal = 3 3