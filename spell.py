from collections import Counter
import itertools

def edits(w):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = set()

    for i in range(len(w)):
        s.add(w[:i]+w[i+1:])   # delete

    for i in range(len(w)):
        for c in letters:
            s.add(w[:i]+c+w[i+1:])   # replace

    for i in range(len(w)-1):
        s.add(w[:i]+w[i+1]+w[i]+w[i+2:])   # swap

    for i in range(len(w)+1):
        for c in letters:
            s.add(w[:i]+c+w[i:])   # insert

    return s

def correct(w, d):
    if w in d:
        return w

    # 1-edit candidates
    e1 = edits(w)
    cand1 = [c for c in e1 if c in d]
    if cand1:
        return max(cand1, key=lambda x: d[x])

    # 2-edit candidates
    e2 = set(e2w for e1w in e1 for e2w in edits(e1w))
    cand2 = [c for c in e2 if c in d]
    if cand2:
        return max(cand2, key=lambda x: d[x])

    return w

# input
text = input("Corpus: ").lower().split()
d = Counter(text)

n = int(input("Words: "))
for _ in range(n):
    w = input().lower()
    print(correct(w,d))
    print()

# Corpus: this is a simple test this test is easy
# Words: 2
# tets
# simplw