
def collatz(sayi):
    maksimum_sayi = sayi
    while(sayi!=1):
        if(sayi%2==0):
            sayi=sayi//2
            if(maksimum_sayi<sayi):
                maksimum_sayi=sayi
        else:
            sayi = sayi*3+1
            if(maksimum_sayi<sayi):
                maksimum_sayi=sayi
    return maksimum_sayi
    
sayi=int(input("Sayi: "))
sonuc = collatz(sayi)
print(sonuc)