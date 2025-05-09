
toplam=0
l=[]
for i in range(1,1000):
    toplam=0
    for j in str(i):
        toplam+=int(j)**len(str(i))
    if(toplam==int(i)):
        l.append(int(i))
print(l)
