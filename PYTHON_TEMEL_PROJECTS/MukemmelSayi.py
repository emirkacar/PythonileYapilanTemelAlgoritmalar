
#Bir sayının mukemmel sayi olup olmadıgını sorgulayan program
def mukemmelSayi(sayi):
    toplam = 0
    for i in range ( 1,sayi):
        for j in range (1,i):
            if ( i % j == 0):
                toplam+=j
    if(toplam == sayi):
        return True



n = int(input("N sayisini giriniz: "))

if (mukemmelSayi(n)):
    print("N sayisi mukemmel sayidir.")
else:
    print("N sayisi mukemmel sayi degildir.")

#Parametre olarak gonderilen sayiya kadar olan mukemmel sayilari ekrana bastiran program

def f():
    mukemmelSayilarListesi = []
    x = 1000
    
    for i in range(1,1001):
        toplam = 0 
        for j in range(1,i):
            if(i % j == 0):
                toplam+=j
        if(toplam == i):
            mukemmelSayilarListesi.append(i)
    print(mukemmelSayilarListesi)


f()


