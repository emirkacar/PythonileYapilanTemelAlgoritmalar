def toplam(liste):
    tekSayilar=[]
    ciftSayilar=[]
    sonucListesi=[]
    toplam=0

    for i in liste:
        if(i%2==0):
            ciftSayilar.append(i)
        else:
            tekSayilar.append(i)
    for i in ciftSayilar:
        toplam+=i
    sonucListesi.append(toplam)
    toplam=0
    for i in tekSayilar:
        toplam+=i
    sonucListesi.append(toplam)

    return sonucListesi

liste=[1,7,4,11,5,0]
print(toplam(liste))