
def algoritma(l):
    n=len(l)
    for i in range(n):
        for j in range(i+1,n):
            if(l[i]%2==1 and l[j]%2==1):
                if(l[i] > l[j]):
                    l[i],l[j] = l[j],l[i]
    return l


sonuc=algoritma([5,8,6,3,4])
print(sonuc)