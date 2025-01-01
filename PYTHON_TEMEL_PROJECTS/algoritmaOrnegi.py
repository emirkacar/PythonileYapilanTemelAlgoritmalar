




l = ["cat","dog","batman","ok","bats","map"]
d = {}
yeniDict = {}

for i in l:
    d[i]= len(i)

print(d)
keys=list(d.keys())
values=list(d.values())

for i in range(len(keys)):
    for j in range(len(values)-1):
        if(values[j] > values[j+1]):
            values[j],values[j+1]=values[j+1],values[j]
            keys[j],keys[j+1]=keys[j+1],keys[j]
print(values)
print(keys)
x={}
frekans = {}

for i,j in zip(keys,values):
    x[i]=j
for k,v in x.items():
    uzunluk = len(k)
    if(uzunluk not in frekans):
        frekans[uzunluk] = []
    frekans[uzunluk].append(k)
print(frekans)



    




