# 3 TANE IYI SORU VAR




"""bakiye=0.0
   sonBakiye=0.0


while(True):
    x=input("Bir rakam giriniz: ")
    if(x=='q'):
        break
    if(x=='1'):
        bakiye=float(input("Ne kadar paraniz var :"))
    if(x=='2'):
        paraYatirma=float(input("Ne kadar para yatiracaksiniz?"))
        sonBakiye=bakiye-paraYatirma
    if(x=='3'):
        paraCekme=float(input("Ne kadar para cekeceksiniz: "))
        if(paraCekme<=bakiye):
            sonBakiye=bakiye+paraCekme

print(bakiye)
print(sonBakiye) """







# MUKEMMEL SAYIYI BULAN ALORİTMA
"""x=int(input("Lutfen bir sayi giriniz:"))
toplam=0 

for i in range (x+1):
    if((x+1) % (i+1)== 0):
        toplam+=i
if(toplam==x):
    print("{} mukemmel sayidir.".format(x))"""






#BIR SAYININ ARMSTRONG SAYI OLUP OLMADIGINI BULAN ALGORİTMA
"""sayi=input("Bir sayi giriniz: ")
gecici=int(sayi)
sayac=0

while(gecici != 0):
    gecici//=10
    sayac+=1
print("Sayi {} basamaklidir.".format(sayac))
gecici=int(sayi)
i=0
toplam=0
while(i<sayac):
    birler=gecici%10
    toplam+=(birler**sayac)
    gecici//=10
    i+=1
if(toplam==int(sayi)):
    print("{} sayisi armstrong sayidir.".format(sayi))"""













