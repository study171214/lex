import math
import re
from collections import Counter

def prep(t):
    return re.findall(r"[a-z]+", t.lower())

# original docs (keep a copy for display)
raw_docs = [
    "I like apple",
    "Apple is good",
    "I like orange",
    "Orange is sweet",
    "I like Banana",
    "Banana is Big" 
]

docs = [prep(d) for d in raw_docs]

# vocab
v = list(set(word for d in docs for word in d))

# df
df = {t: 0 for t in v}
for t in v:
    for d in docs:
        if t in d:
            df[t] += 1

N = len(docs)

# tf-idf
vec = []
for d in docs:
    tf = Counter(d)
    temp = []
    for t in v:
        temp.append(tf[t] * math.log(N / df[t]))
    vec.append(temp)

# cosine similarity
def cos(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    n1 = math.sqrt(sum(x*x for x in a))
    n2 = math.sqrt(sum(x*x for x in b))
    return dot/(n1*n2) if n1 and n2 else 0

# compare with doc1
base_doc = 0
scores = []

print("\n🔍 Comparing with:", raw_docs[base_doc])
print("-" * 50)

for i in range(1, N):
    score = cos(vec[base_doc], vec[i])
    scores.append((i, score))
    print(f"Doc {i+1}: \"{raw_docs[i]}\" → Similarity = {score:.4f}")

# best match
best = max(scores, key=lambda x: x[1])

print("\n Most similar document:")
print(f"Doc {best[0]+1}: \"{raw_docs[best[0]]}\"")
print(f"Similarity Score: {best[1]:.4f}")
