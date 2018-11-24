import numpy as np

def make_homomorphisms(a1, a2):

    if(len(a1)==1):
        return [[a1[0], i] for i in a2]

    n1 = len(a1)
    n2 = len(a2)

    if (n1 == n2):
        isomorphisms = make_isomorphisms(a1, a2)
        return isomorphisms

    else :
        a2 = extesions(a2, n1-n2)
        homomorphisms = []
        for j in a2:
            homomorphisms = homomorphisms + make_isomorphisms(a1, j)
        return homomorphisms

def make_isomorphisms(a1, a2):
    if(len(a2)==1):
        return [[(i, a2[0])] for i in a1]

    head = a2[0]
    tail = a2[1:]

    isomorphisms = []

    for i in range(len(a1)):
        rem = np.delete(a1, i)
        t   = make_isomorphisms(rem, tail)
        for j in t:
            isomorphisms.append([(a1[i],head)] + j)

    return isomorphisms

def extesions(a, n):
    t = extensions_helper(a,n)
    print(t)
    ext = []
    for j in t:
        ext.append(a + j)
    print(ext)
    return ext

def extensions_helper(a,n):
    if(n==1):
        return [[i] for i in a]

    else:
        t    = extensions_helper(a, n-1)
        exts = []
        for i in a:
            for k in t:
                exts.append([i] + k)

        return exts

def transform(pred, homomorphism):
    return [homomorphism[i][1] for i in pred]


def accuracy(pred, y, n1, n2):
    a1 = range(n1)
    a2 = range(n2)

    homomorphisms = make_homomorphisms(a1, a2)
    n = len(pred)

    accuracy = 0
    for homomorphism in homomorphisms:
        predp = transform(pred, homomorphism)
        accuracy = max(accuracy, np.sum([(predp[i]==y[i]) for i in range(n)])/n)

    return accuracy

print(len(make_homomorphisms([1,2,3,4,5], [1,3,4,5,2])))
