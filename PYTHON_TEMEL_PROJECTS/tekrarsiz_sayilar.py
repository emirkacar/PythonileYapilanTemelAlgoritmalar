


def tekrarsizSayilar(l):
    liste = []
    lngt=len(l)
    d={}
    z={}
    for i in range(lngt):
        liste.append(l[i])
    for i in liste:
        d[i] = liste.count(i)
    for k,v in d.items():
        if(v==1):
            z[k] = v
    return z

y = tekrarsizSayilar([1, 2, 2, 3, 4, 4, 5]) 
print(y)