



l = [1,6,3,4,4,2,5,5,1]
tekrarli_elemanlar = []
n = len(l)

for i in range(n):
    for j in range(i+1,n):
        if(l[i]==l[j]):
            tekrarli_elemanlar.append(l[i])
print(tekrarli_elemanlar)

