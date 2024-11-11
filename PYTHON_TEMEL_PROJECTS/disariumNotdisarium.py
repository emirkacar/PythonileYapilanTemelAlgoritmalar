
sayi = input("Sayi: ")
sayac = 1
toplam=0

for i in sayi:
    toplam+=(int(i)**sayac)
    sayac+=1
if(toplam==int(sayi)):
    print("disarium")
else:
    print("notdisarium")
