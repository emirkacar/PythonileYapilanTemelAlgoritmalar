#Faktoriyel hesaplama
carpim = 1
sayi = int(input("Faktoriyeli alinacak sayiyi giriniz: "))

for i in range(1,sayi+1):
    carpim*=i
print("%d sayisinin faktoriyeli = %d" % (sayi,carpim))


#Fibonacci serisi hesaplama
a=1
b=1
c=a+b
print(a,b,c,end=" ")
for i in range (5):
    a=b
    b=c
    c=a+b
    print(c,end=" ")


#Asal sayı Bulma

sayi = int(input("Hangi sayiya kadar olan asal sayilari yazdirmak istiyorsun? "))

if ( sayi < 2):
    asal=False
else:
    for i in range(2,sayi+1):
        asal = True
        for j in range (2,i):
            if(i%j == 0):
                asal=False
                break
        if(asal==True):
            print("%d sayisi asaldir." % (i))




#Liste elemanlarinin toplami

liste = [1, 2, 3, 4, 5]
toplam = 0

for i in liste:
    toplam+=i
print(toplam)


#Ters ceviren program 1.Yol

metin = input("Bir metin girin: ")

tersCevrilmisHali = metin[::-1]
print(tersCevrilmisHali)


#Ters ceviren program 2.Yol

metin = input("Bir metin girin: ")
uzunluk = len(metin)    
tersMetin = ""

for i in range (uzunluk-1,-1,-1):
    tersMetin+=metin[i]
print("Metnin ters cevrilmis hali :")
print(tersMetin)


#Carpim Tablosu

for i in range(1,10):
    for j in range(1,10):
        print("%d x %d = %d" % (i,j,i*j))
    print()


#Bir metin içinde karakterlerin kaç kez geçtiğini bulan ve sozluge atan program

metin=input("Bir metin giriniz : ")
sozluk ={}

for i in metin:
    if( i not in sozluk):
        sozluk.update( {i:1})
    else:
        sozluk[i]+=1
print(sozluk)



#Bir metin içinde belirli bir karakterin kaç kez geçtiğini bulan program    

metin=input("Bir metin giriniz : ")
harf = input("Hangi harfin kac kez gectigini bulmak istiyorsunuz? :")
sayac = 0

for i in metin:
    if (harf == i):
        sayac+=1
print(f"{harf} harfi {sayac} kez tekrarlanmistir.")

#Palindrom kontrolu

sayi = int(input("Palindrom kontrolu yapilacak sayiyi giriniz: "))
stringSayi = str(sayi)


for i in range(len(stringSayi)):
    palindrome = 1
    if stringSayi[i] != stringSayi[-(i + 1)]:
        palindrome = 0
        break
if(palindrome):
    print("Sayi palindromdur.")
else:
    print("Sayi palindrom degildir.")

    















    



