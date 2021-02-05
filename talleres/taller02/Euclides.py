def gcd_euclid(p, q):
    if p%q == 0:
        return q
    else:
        division = int(p/q)
        residuo = p-(division*q)
        return gcd_euclid(q,residuo)

print(gcd_euclid(848, 656))