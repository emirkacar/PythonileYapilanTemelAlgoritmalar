#1.ORNEK
def islem(secim,*args):

    
        def carp():
            carp = 1
            for i in args:
                carp *= i
            return carp
        def topla():
            topla = 0
            for i in args:
                topla += i
            return topla
        
        if(secim == "carp"):
            print(carp())
        elif(secim == "topla"):
            print(topla())
        else:
             print("Gecersiz islem.")

liste = [1,2,3,4,5,6,7,8,9,10]
secim = input("Seciminizi giriniz (topla,carp): ")
sonuc = islem(secim,*liste)






#2.ORNEK 
def hesaplamalar(sayi):

    def kareAl(x):
        return x**2
    
    
    
    def faktoriyel(x):

        sonuc = 1
        while(x > 0):
            sonuc *= x
            x -= 1
        return sonuc    

    karesi = kareAl(sayi)
    fakt = faktoriyel(sayi)

    return (f"Karesi = {karesi} faktoriyeli = {fakt}")

print(hesaplamalar(6))

