
def siraliMiMutlakFark(l):
    uzunluk = len(l)
    z=[]
    for i in range(uzunluk-1):
        fark = abs(l[i] - l[i+1])
        z.append(fark)
    for i in range(uzunluk-1):
        kontrol=1
        if(l[i] > l[i+1]):
            kontrol=0
            return False
    if(kontrol==1):
        return True
sonuc=siraliMiMutlakFark([1, 2,4,7]) 
print(sonuc)