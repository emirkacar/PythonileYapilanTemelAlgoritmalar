


def closeThe(demet):
    l = list(demet)
    n=len(l)
    x=[]
    sayac=0
   
    for i in range(1,n):
        if(sayac==n//2):
            break
        x.append([l[i-1],l[n-i]])
        sayac+=1
    if(n%2==1):
        x.append([l[sayac],l[sayac]])
    return x

demet = (1,2,3,4,5,6)
sonuc=closeThe(demet)
print(sonuc)