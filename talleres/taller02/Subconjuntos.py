def subconjuntos(s):
    subconjuntosBase("", s)

def subconjuntosBase(base, t):
    if len(t) == 0:
        print(base)
    else:
        x = t[1:]
        subconjuntosBase(base+ t[:1], x)
        subconjuntosBase(base,x) 

print(subconjuntos("abc"))