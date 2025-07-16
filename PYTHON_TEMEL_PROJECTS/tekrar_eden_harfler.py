def tekrarEdenHarfler(metin):
    metin_liste = list(metin)
    d={}
    for harf in metin_liste:
        if(harf not in d):
            d[harf] = 1
        else:
            d[harf] +=1
    d_values = list(d.values())
    d_keys=list(d.keys())
    for k,v in d.items():
        if(v>1):
            hedef = k
    hedef = list(hedef)
    return hedef
sonuc=tekrarEdenHarfler("tekrar") 
print(sonuc)