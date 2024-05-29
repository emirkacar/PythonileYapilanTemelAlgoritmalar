#1.Yol (Collatz Sanısı)
n = int(input("n: "))
sayac = 0
while(True):
    sayac+=1 
    if (n %2 ==0):
        n = n/2  
    elif(n % 2 == 1):
        n = (3*n)+1  
    if(n == 1):
        sayac+=1
        break
print("%d.adimda 1 sayisina ulasilmistir." % (sayac))



#2.Yol (Collatz Sanısı)
n = int(input("n: "))
sayac = 0

while(n != 1):
    sayac+=1 
    print(n , end=" ")
    if (n %2 ==0):
        n = n//2  
    else:
        n = (3*n)+1  
print(n)
print("%d.adimda 1 sayisina ulasilmistir." % (sayac))


#3.Yol (Collatz Sanısı)

def collatz(i):
    sayac = 0
    while(i != 1):
        sayac+=1 
        if (i %2 ==0):
            i = i//2  
        else:
            i = (3*i)+1  
    return sayac 

maxUzunluk = 0
maxSayi = 0
for i in range(1,100):
    sonuc = collatz(i)
    if(maxUzunluk<sonuc):
        maxUzunluk = sonuc
        maxSayi = i
print("Maksimum uzunluk = %d , sayisi %d'dir" % (maxUzunluk,maxSayi))




# 4.Yol (Collatz Sanisinin serisini bulma)


def collatz(i):
    seri = []
    sayac = 0
    while(i != 1):
        seri.append(i)
        if (i %2 ==0):
            i = i//2  
        else:
            i = (3*i)+1  
    seri.append(i)
    return seri

maxUzunluk = 0
maxSayi = 0
maxSeri = []

for i in range(1,100):
    sonuc = collatz(i)
    if(len(maxSeri) < len(sonuc)):
        maxSeri = sonuc
        maxSayi = i
        maxUzunluk = len(sonuc)
print(f"Maximum sayi {maxSayi} , maximum seri {maxSeri},maximum uzunluk {maxUzunluk}")










