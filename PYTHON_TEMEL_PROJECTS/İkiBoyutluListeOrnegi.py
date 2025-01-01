l = ["cat","dog","bat"]
d = {}
uzunluk = len(l)

for i in range(uzunluk):
    for j in range(uzunluk):
        if(j not in d):
            d[j] = []
        d[j].append(l[i][j])

for k,v in d.items():
    print(k,v)


        
    

