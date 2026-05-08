def fix(s):
    words = s.split()
    res = []

    for w in words:
        if w.endswith("/??"):
            res.append(w.replace("/??","/NN"))
        elif w.endswith("/???"):
            res.append(w.replace("/???","/VBN"))
        else:
            res.append(w)

    return " ".join(res)

s = input("Sentence: ")
print(fix(s))

# Sentence: this is my//?? world//???
# this is my//NN world//VBN