import itertools

def solve(words, res):
    l = list(set(''.join(words)+res))

    if len(l) > 10:
        print("Too many letters")
        return

    for p in itertools.permutations(range(10), len(l)):
        m = dict(zip(l,p))

        if any(m[w[0]]==0 for w in words+[res]):
            continue

        vals = []
        for w in words:
            vals.append(int(''.join(str(m[c]) for c in w)))

        r = int(''.join(str(m[c]) for c in res))

        if sum(vals) == r:
            print("\nSolution:", m)
            print(" + ".join(map(str,vals)), "=", r)
            return

    print("No solution")

# input
n = int(input("Words: "))
w = [input().upper() for _ in range(n)]
res = input("Result: ").upper()

solve(w,res)

# Words: 2
# SOME
# TIME
# Result: SPENT