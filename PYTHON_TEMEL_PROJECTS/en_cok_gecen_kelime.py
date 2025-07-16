def enCokGecenKelime(metin):
    metin_liste = metin.split()
    d={}

    for i in metin_liste:
        if(i not in d):
            d[i] = 1
        else:
            d[i] += 1
    d_keys = list(d.keys())
    d_values = list(d.values())
    
    max=d_values[0]
    for i in d.values():
        if(max < i):
            max=i
            
    for k,v in d.items():
        if(max==v):
            max_key = k
    return max_key,max
    

sonuc=enCokGecenKelime("elma armut elma muz elma muz")
print(sonuc)