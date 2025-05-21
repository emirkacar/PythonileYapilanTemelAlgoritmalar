
def ebob(x,y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i==0):
            ebob=i
        i+=1
    return ebob
    
sonuc=ebob(8,360)
print(sonuc)