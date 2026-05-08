def fill(sentence):
    words = sentence.split()
    tags = set()

    # collect existing tags
def fill(sentence):
    words = sentence.split()
    res = []

    for w in words:
        if '??' in w:
            word = w.split('/')[0]

            if word.lower() in ['my','your','his','her']:
                tag = 'PRP$'   # possessive pronoun
            elif word.lower() in ['is','am','are']:
                tag = 'VBZ'
            elif word.lower() in ['world','system','space']:
                tag = 'NN'
            else:
                tag = 'NN'

            res.append(word+'/'+tag)
        else:
            res.append(w)

    return " ".join(res)

# input
s = input("Sentence: ")

print(fill(s))

# Sentence: People/NNS continue/VBP to/TO inquire/VB the/DT reason/?? for/IN the/DT race/NN for/IN outer/JJ space/??