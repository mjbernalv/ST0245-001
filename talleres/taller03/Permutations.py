def permutations(base, stri):
    if len(stri)==0:
        print(base) 
    else:
        for i in range (len(stri)):
            permutations(base+stri[i], stri[0:i] + stri[i+1:])

permutations("", "abc")