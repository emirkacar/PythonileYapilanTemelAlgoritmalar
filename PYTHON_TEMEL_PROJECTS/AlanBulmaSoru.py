tip = int(input("Geometrik sekli seciniz :(1:Ucgen 2:Dikdortgen) "))
taban= int(input("Veri1 : "))
yukseklik = int(input("Veri1 : "))

if(tip==1):
    print(f"Ucgenin alani: {(taban*yukseklik)/2}")
elif(tip==2):
    print(f"Dikdortgenin alani : {taban*yukseklik}")
else:
    print("1-2 arasinda deger giriniz. ")




