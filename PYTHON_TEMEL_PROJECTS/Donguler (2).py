# KULLANICIDAN POZİTİF TAM SAYI ALAN VE BU SAYININ RAKAMLARININ CARPIMINI BASAN ALGORİTMA
""" x=input("Lutfen pozitif bir tam sayi giriniz.")
carpim=1
i=0

while(int(x)<=0):
    x=input("Lutfen pozitif bir tam sayi giriniz.")
while(i < len(x)):
        carpim*=int(x[i])
        i+=1
       
print("x sayisinin rakamlarinin carpimi : ",carpim) """

#IKINCI YOL

x=int(input("Bir sayi girin"))
gecici=x
carpim=1

while (x < 0):
    x=int(input("Bir sayi girin"))
while(gecici != 0):
    carpim*= (gecici % 10)
    gecici//=10
print(carpim)


