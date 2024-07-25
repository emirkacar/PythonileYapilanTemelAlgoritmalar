import time
import random

randomSayi=random.randint(1,100)
tahminSayisi = 10
sayac = 0
oncekiTahminler = []
while(tahminSayisi>0):
    sayi = int(input("1-100 arasinda bir deger giriniz: "))
    if(sayi > randomSayi):
        if(sayi in oncekiTahminler):
            print("Bu sayiyi onceden tahmin etmistiniz.")
            tahminSayisi -= 1
            sayac+=1
            print(f"Kalan tahmin hakkiniz:{tahminSayisi}")
            print(oncekiTahminler)
        else:
            tahminSayisi-=1
            print("Tahmininizi azaltin")
            oncekiTahminler.append(sayi)
            sayac+=1
            print(f"Kalan tahmin hakkiniz:{tahminSayisi}")
            print(oncekiTahminler)
    elif(sayi==randomSayi):
        print(f"{10-tahminSayisi}. denemede dogru sayiyi buldunuz,tebrikler!")
        print(oncekiTahminler)
        break
    
    else:
        if(sayi in oncekiTahminler):
            print("Bu sayiyi onceden tahmin etmistiniz.")
            oncekiTahminler.append(sayi)
            tahminSayisi -= 1
            sayac+=1
            print(f"Kalan tahmin hakkiniz:{tahminSayisi}")
            print(oncekiTahminler)
        else:
            tahminSayisi-=1
            print("Tahmininizi arttirin.")
            oncekiTahminler.append(sayi)
            sayac+=1
            print(f"Kalan tahmin hakkiniz:{tahminSayisi}")
            print(oncekiTahminler)
    if(tahminSayisi==0):
        print(f"Üzgünüm, tahmin hakkiniz bitti. Doğru sayi {randomSayi} idi.")
    
    if(tahminSayisi>0):
       secim=input("Oynamak istiyor musunuz?(Evet,Hayir)")
       
    if(secim=="Evet"):
        continue
    else:
        break
        
        
        
       