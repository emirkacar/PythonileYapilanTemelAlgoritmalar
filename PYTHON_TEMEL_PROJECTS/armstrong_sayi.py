

sayi = int(input("Sayi: "))
toplam=0
deger = str(sayi)
for i in deger:
    toplam+=int(i)**len(deger)
if(toplam==sayi):
    print(f"{sayi} armstrong sayidir")
else:
    print(f"{sayi} armstrong sayi degildir")