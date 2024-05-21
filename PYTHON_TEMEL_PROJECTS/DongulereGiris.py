 #SAYİ 0'DAN BUYUK OLUNCAYA KADAR KULLANICIDAN DEGER ISTEYEN ALGORİTMA
sayi=int(input("Lutfen bir pozitif tam sayi giriniz."))

while ( sayi < 0):
    print("Sayiniz negatif,lutfen pozitif tam sayi giriniz")
    sayi=int(input("Lutfen pozitif tam sayi giriniz."))
print("Program basariyla sonuclanmistir ve sayinin degeri =",sayi) 


# Bu algoritma 0'dan 100'e kadar olan sayilarin toplamini verir.
x=0
toplam=0

while(x<100):
    toplam+=x
    x+=1
print("0'dan 100'e kadar olan sayilarin toplaminin degeri : ",toplam ) 


#X 3'DEN BUYUK ESİT OLDUGUNDA DONGU SONLANIYOR.
x = 0
while (1):
    print(x)
    x += 1
    if (x >= 3):
        break 








#X'E DEGER OLARAK 0 GIRILDIGINDE DONGU SONLANIYOR.0 GIRILENE KADAR OLAN SAYILARIN TOPLAMINI VEREN ALGORİTMA.
toplam =0

while (1):
    x=int(input("Lutfen tam sayi giriniz."))
    toplam += x
    if(x==0):
        break
print("Toplam degeri = ",toplam) 







 #FAKTORIYEL HESABI
 x=int(input("Bir sayi giriniz.")) 
faktoriyel=1

while(x>0):
    faktoriyel*=x
    x-=1

print("Faktoriyelin sonucu : ",faktoriyel) 








#CIFT TEK SAYI BULMA
x=float(input("Bir sayi giriniz"))

while(1):
    x=float(input("Bir sayi giriniz"))
    if(x==0):
        break
    if(x%2==0):
        print(" : Cift",x)
    else:
        print(" : Tek",x)   










 #BIR SAYININ USSUNU BULAN ALGORITMA.
 taban = float(input("Taban giriniz : "))
us = float (input("Us giriniz: "))
sonuc =1

while (us != 0):
    sonuc*=taban
    us-=1


print("Sonuc = ",sonuc ) 










 #SAYININ TERSI
 sayi=int(input("Bir sayi giriniz: "))
sayininTersi = 0

while(sayi != 0):
    birler=sayi%10
    sayininTersi=(sayininTersi*10)+birler
    sayi//=10

print("Sayinin tersi = ",sayininTersi) 







#SAYININ TERSI
sayi=int(input("Bir sayi giriniz: "))
ters = str(sayi)[-1::-1]
print(ters)





# ASAL SAYI ALGORİTMASI
 sayi=2

while(1):
    i=2
    asal=True
    while(i<=sayi**0.5):
        if(sayi % i ==0):
            asal=False
            break
        i+=1
    

    if(asal):
        print(sayi,"bir asal sayidir.")
    sayi+=1

    cikis=input("Devam etmek istiyor musunuz?(E,H)")
    if(cikis=='H'):
        break 










 #0'DAN 100'E KADAR OLAN SAYILARIN TOPLAMI
 toplam =0

for x in range(100):
    toplam+=x
print(toplam)






 







i = 0

while(i<10):
    if(i==3 or i==5):
        continue
    print(i)
    i+=1





#Belirli bir deger araligindaki asal sayilari bastirma algoritması
sayi=int(input("Lutfen bir sayi giriniz."))

if(sayi < 2):
    print("2'den kucuk sayilar asal sayi degildir.")
else :
    for i in range (2,sayi):
        asal=True
        for num in range (2,i):
            if(i%num == 0):
                asal=False
        if(asal):
            print(i) 





#FİBONACCİ SAYISI ALGORİTMASI
 a, b = 0, 1


while(a<22):
    print(a)
    c=a+b
    a=b
    b=c 



for i in range(101,1,-1):
    print(i)  


#CARPİM TABLOSU
for i in range (1,11):
    for j in range (i,11):
        print(i,"x",j,"=",i*j) 





#IYI BIR ORNEK
 sayi=int(input("Sayi: "))
sayac=0

while(sayi>1):
    if(sayi%2==0):
        sayi=(sayi/2)
        print(sayi)
        sayac+=1
    else:
        sayi=(sayi*3)+1
        print(sayi)
        sayac+=1
print(sayi)
print("Kac kere dongude dondu? ",sayac) 




 x=int(input("Sayi giriniz : "))
rakamlarinToplami=0
temp=x

while(temp != 0):
    rakamlarinToplami += (temp%10)
    temp//=10
print(rakamlarinToplami)
if((x%rakamlarinToplami)==0):
    print("Harshad")
else:
    print("Notharshad") 






#Sayının tersini alan algoritma
 x=int(input("Sayi girin: "))
gecici=x
sayininTersi = 0

while( gecici != 0):
    birler = gecici % 10
    sayininTersi=(sayininTersi*10)+birler
    gecici//=10
print(sayininTersi) 














    

    



        




    














    
