import heapq
import matplotlib.pyplot as plt
import math

def astar(g,h,s,goal):
    pq=[(0,s)]
    cost={s:0}
    parent={s:None}

    while pq:
        _,cur=heapq.heappop(pq)
        if cur==goal:
            break
        for nb,w in g[cur]:
            new=cost[cur]+w
            if nb not in cost or new<cost[nb]:
                cost[nb]=new
                f=new+h[nb]
                heapq.heappush(pq,(f,nb))
                parent[nb]=cur

    path=[]

    cur=goal

    while cur:
        path.append(cur)
        cur=parent[cur]
    path.reverse()
    return path,cost[goal]


n=int(input("Cities: "))

g={}

for _ in range(n):
    c=input("City: ")
    g[c]=[]

e=int(input("Edges: "))

edges=[]

for _ in range(e):
    a,b,w=input("A B dist: ").split()
    w=int(w)
    g[a].append((b,w))
    g[b].append((a,w))
    edges.append((a,b,w))

h={}

print("Heuristic:")

for c in g:
    h[c]=int(input(c+": "))

s=input("Start: ")
goal=input("Goal: ")
path,cost=astar(g,h,s,goal)
print("\nPath:",path)
print("Cost:",cost)


plt.figure(figsize=(7,7))
pos={}
radius=5
nodes=list(g.keys())

for i,node in enumerate(nodes):
    angle=2*math.pi*i/len(nodes)
    x=radius*math.cos(angle)
    y=radius*math.sin(angle)
    pos[node]=(x,y)

for a,b,w in edges:
    x1,y1=pos[a]
    x2,y2=pos[b]

    if a in path and b in path:
        ai=path.index(a)
        bi=path.index(b)

        if abs(ai-bi)==1:
            plt.plot(
                [x1,x2],
                [y1,y2],
                linewidth=4
            )

        else:
            plt.plot(
                [x1,x2],
                [y1,y2],
                linestyle='dashed'
            )

    else:
        plt.plot(
            [x1,x2],
            [y1,y2],
            linestyle='dashed'
        )
    mx=(x1+x2)/2
    my=(y1+y2)/2
    plt.text(mx,my,str(w),fontsize=12)

for node in nodes:
    x,y=pos[node]

    if node in path:
        plt.scatter(x,y,s=2500)

    else:
        plt.scatter(x,y,s=2000)

    plt.text(
        x,
        y,
        f"{node}\nh={h[node]}",
        ha='center',
        va='center',
        fontsize=12,
        color='white'
    )
plt.title("A* Search Graph")
plt.axis('off')
plt.show()

# Cities: 4
# City: A
# City: B
# City: C
# City: D
# Edges: 4
# A B dist: A B 1
# A B dist: B C 2
# A B dist: C D 3
# A B dist: A D 7
# Heuristic:
# A: 6
# B: 4
# C: 2
# D: 0
# Start: A
# Goal: D