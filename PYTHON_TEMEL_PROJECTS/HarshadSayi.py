

sayi=int(input("Sayi: "))
gecici = sayi
liste=[] 
toplam=0

while(gecici!=0):
    kalan = gecici%10
    gecici//=10
    liste.append(kalan)

for i in liste:
    toplam+=i
if(sayi%toplam==0):
    print("Harshad")
else:
    print("Notharshad")


