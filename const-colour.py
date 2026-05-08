import matplotlib.pyplot as plt
import math

def safe(n,c,a,g):
    for nb in g[n]:
        if a.get(nb)==c:
            return False
    return True

def solve(g,colors,a,nodes,i):
    if i==len(nodes):
        return True
    node=nodes[i]
    for c in colors:
        if safe(node,c,a,g):
            a[node]=c
            if solve(g,colors,a,nodes,i+1):
                return True
            del a[node]
    return False

n=int(input("Regions: "))
g={}

for _ in range(n):
    node=input("Region: ")
    g[node]=input("Neighbors: ").split()
colors=input("Colors: ").split()

a={}

nodes=list(g.keys())

if solve(g,colors,a,nodes,0):
    print("\nAssignment:")
    for k in a:
        print(k,"->",a[k])
    plt.figure(figsize=(6,6))
    pos={}
    radius=5

    for i,node in enumerate(nodes):
        angle=2*math.pi*i/len(nodes)
        x=radius*math.cos(angle)
        y=radius*math.sin(angle)
        pos[node]=(x,y)

    for node in g:
        x1,y1=pos[node]

        for nb in g[node]:
            if nb in pos:
                x2,y2=pos[nb]
                plt.plot([x1,x2],[y1,y2])

    for node in nodes:
        x,y=pos[node]
        plt.scatter(x,y,s=3000,c=a[node])
        plt.text(x,y,node,
                 ha='center',
                 va='center',
                 fontsize=14,
                 color='white')

    plt.axis('off')
    plt.title("Map Coloring Graph")
    plt.show()
else:
    print("No solution")

#     Regions: 4
# Region: A
# Neighbors: B C
# Region: B
# Neighbors: A C D
# Region: C
# Neighbors: A B D
# Region: D 
# Neighbors: B C
# Colors: Red Green Blue