#ASAL SAYİ ALGORİTMASI
sayi=int(input("Bir sayi giriniz"))


for i in range(2,sayi):
    asal=True
    for j in range(2,i):
        if(i%j==0):
            asal=False
            break
    if(asal):
        print("{} sayisi asal bir sayidir.".format(i))    