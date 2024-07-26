def f(sayi):
    toplam=0
    gecici=sayi
    while(gecici>0):
        kalan=gecici%10
        toplam+=kalan
        gecici//=10

    if(toplam%2!=0):
        return f(toplam)
    else:
        return toplam
    
sayi=int(input("Sayi: "))
print(f(sayi))