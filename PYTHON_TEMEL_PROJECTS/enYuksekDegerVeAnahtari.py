sozluk = {'elma': 50, 'armut': 75, 'kiraz': 90, 'muz': 60}


maks_deger = sozluk['elma']
for k,v in sozluk.items():
    if(maks_deger<sozluk[k]):
        maks_deger=sozluk[k]
        maks_key = k
print(maks_deger,maks_key)
