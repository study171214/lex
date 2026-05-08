import heapq, math
import matplotlib.pyplot as plt

def h(c,a,b):
    x1,y1 = c[a]
    x2,y2 = c[b]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def best_first(g,c,s,goal):
    heap = [(h(c,s,goal), s, [s], 0)]
    v = set()

    while heap:
        _,cur,path,cost = heapq.heappop(heap)

        if cur in v:
            continue

        v.add(cur)

        if cur == goal:
            return path, cost

        for nb,w in g[cur]:
            if nb not in v:
                heapq.heappush(
                    heap,
                    (h(c,nb,goal), nb, path+[nb], cost+w)
                )

n = int(input("Cities: "))

c = {}

for _ in range(n):

    name = input("Name: ")

    x,y = map(float,input("x y: ").split())

    c[name]=(x,y)

e = int(input("Edges: "))

g = {k:[] for k in c}

edges=[]

for _ in range(e):

    a,b,d = input("A B dist: ").split()

    d = float(d)

    g[a].append((b,d))

    g[b].append((a,d))

    edges.append((a,b,d))

s = input("Start: ")

goal = input("Goal: ")

path,cost = best_first(g,c,s,goal)

print("\nPath:", path)

print("Cost:", cost)


plt.figure(figsize=(8,8))

for a,b,d in edges:

    x1,y1 = c[a]

    x2,y2 = c[b]

    if a in path and b in path:

        ai = path.index(a)

        bi = path.index(b)

        if abs(ai-bi)==1:

            plt.annotate(
                "",
                xy=(x2,y2),
                xytext=(x1,y1),
                arrowprops=dict(
                    arrowstyle="->",
                    lw=3
                )
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

    mx = (x1+x2)/2

    my = (y1+y2)/2

    plt.text(mx,my,str(d),fontsize=11)

for city in c:

    x,y = c[city]

    if city in path:

        plt.scatter(x,y,s=2000)

    else:

        plt.scatter(x,y,s=1500)

    plt.text(
        x,
        y,
        city,
        ha='center',
        va='center',
        fontsize=10,
        color='white'
    )

plt.title("Best First Search Graph")

plt.axis('off')

plt.show()




# # Cities: 4
# # City: A
# # City: B
# # City: C
# # City: D
# # Edges: 4
# # A B dist: A B 1
# # A B dist: B C 2
# # A B dist: C D 3
# # A B dist: A D 7
# # Heuristic:
# # A: 6
# # B: 4
# # C: 2
# # D: 0
# # Start: A
# # Goal: D