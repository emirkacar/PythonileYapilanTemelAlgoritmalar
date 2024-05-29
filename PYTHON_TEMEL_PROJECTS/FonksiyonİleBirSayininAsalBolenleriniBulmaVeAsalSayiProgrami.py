#Asal Sayi Bulma
def asalSayi():
    x = 50
    for i in range(2,x):
        asal=True
        for j in range(2,i):
            if(i%j==0):
                asal=False
        if(asal):
            print(i)
asalSayi()





#Bir sayinin tam bolenlerini bulma
tamBolenlerListesi = []
def tamBolenler(x):
    for i in range(2,x+1):
        if(x % i == 0):
            tamBolenlerListesi.append(i)
    return tamBolenlerListesi

sonuc = tamBolenler(10)
print(sonuc)


