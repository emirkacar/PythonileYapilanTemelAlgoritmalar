import math

sayi=int(input("Sayi: "))
liste=[]
sayac=0
tersListe=[]
gecici=sayi

while(gecici!=0):
    kalan=gecici%10   
    liste.append(kalan)
    gecici//=10
    sayac+=1
print(f"Sayi {sayac} basamaklidir.")
tersListe=liste[::-1]

if(pow(tersListe[0],1)+pow(tersListe[1],2)+pow(tersListe[2],3)+pow(tersListe[3],4) == sayi):
    print("Disarium")
else:
    print("Notdisarium")








