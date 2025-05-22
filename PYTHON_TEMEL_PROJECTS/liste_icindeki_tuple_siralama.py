

def kontrol(l):
    n=len(l)
    for i in range(n):
        for j in range(i+1,n):
            if(l[i][-1] > l[j][-1]):
                l[i],l[j] = l[j],l[i]
    return l

sonuc=kontrol([("b",1),("c",2),("x",3),("x",4),("z",0)])
print(sonuc)