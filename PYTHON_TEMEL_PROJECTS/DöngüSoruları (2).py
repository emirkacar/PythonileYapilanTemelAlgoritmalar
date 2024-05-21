#DONGULER ILE BIRLIKTE BİR SAYININ CIFT OLUP OLMADIGINI BULAN ALGORİTMA
sayi=int(input("Lutfen bir tam sayi giriniz."))
toplam=0
sayac=0

for i in range(sayi):
    if(i%2==0):
        print("{} sayisi cift sayidir.".format(i))
        toplam+=i
        sayac+=1
print("Toplam = {}".format(toplam))
print("sayac = {} ".format(sayac))
  