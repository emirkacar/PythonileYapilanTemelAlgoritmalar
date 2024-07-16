from functools import reduce


liste = [1,2,3,4,5,6,7,8,9,10]

def ciftSayilarFonksiyonu(sayi):
    if(sayi%2==0):
        return sayi
    
def toplama(x,y):
    return x+y

ciftSayilar = list(filter(ciftSayilarFonksiyonu,liste))
print(ciftSayilar)

toplam = reduce(toplama,ciftSayilar)
print(toplam)










