

l = ["cat","dogs","batman","ok"]
uzunluk = len(l)
d={}
z = {}

for i,j in enumerate(l):
    if(i not in d):
        d[i]=[]
    d[i].append(j)

values = list(d.values())
print(values)

values_un_uzunlugu = len(values)

for i in range(values_un_uzunlugu):
    for j in values[i]:
        for k in j:
            if(len(j) not in z):
                z[len(j)] = []
            z[len(j)].append(k)
yeniSozluk = {}
sayac = 0
for k,v in z.items():
    for i,j in enumerate(v):
        if(i not in yeniSozluk):
            yeniSozluk[i]=[]
        yeniSozluk[i].append(j)
for k,v in yeniSozluk.items():
    print(k,v)
    


    

    

        

