


def ebob(sayi1,sayi2):
    sayi1_bolen_liste = []
    i=1
    while(i<sayi1):
        if(sayi1%i==0):
            sayi1_bolen_liste.append(i)
        i+=1
    sayi2_bolen_liste = []
    i=1
    while(i<sayi2):
        if(sayi2%i==0):
            sayi2_bolen_liste.append(i)
        i+=1
    maksimum_sayi1_bolen = max(sayi1_bolen_liste)
    maksimum_sayi2_bolen=max(sayi2_bolen_liste)
    if(sayi1>sayi2):
        for i in sayi1_bolen_liste:
            if(i in sayi2_bolen_liste):
                ebob=i
        if(maksimum_sayi2_bolen in sayi1_bolen_liste):
            ebob=maksimum_sayi1_bolen
    elif(sayi2>sayi1):
        for i in sayi2_bolen_liste:
            if(i in sayi1_bolen_liste):
                ebob=i
        if(maksimum_sayi1_bolen in sayi2_bolen_liste):
            ebob=maksimum_sayi1_bolen
    else:
        ebob=sayi1

    return ebob

sonuc = ebob(28,16)
print(sonuc)