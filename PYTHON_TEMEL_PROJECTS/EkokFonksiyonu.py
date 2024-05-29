#Ekok hesaplama programi

def ekok(x,y):
    if (x == y):
        ekok = x
    elif ( x>y):
        kat = x
        while(1):
            if(kat % x == 0 and kat % y == 0):
                ekok = kat
                break
            kat+=1
    else:
        kat = y
        while(1):
            if(kat % x == 0 and kat % y ==0):
                ekok = kat
                break
            kat+=1

    return ekok

sayi1=int(input("Sayi1: "))
sayi2=int(input("Sayi2: "))


sonuc = ekok(sayi1,sayi2)
print("Iki sayinin ekoku = ",sonuc)