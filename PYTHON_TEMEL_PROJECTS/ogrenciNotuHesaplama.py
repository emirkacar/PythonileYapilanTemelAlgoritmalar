def ogrenci_ortalama_hesapla(l):
    d={}
    for i in l:
        toplam = 0
        for j in i:
            if(str(j).isdigit()):
                toplam+=int(j)
        d[i[0]]=toplam//3
    en_yuksek_ortalamaya_sahip_ogrenci = max(d.items(),key=lambda x: x[1])
    return d,en_yuksek_ortalamaya_sahip_ogrenci
    
ogrenciler = [
    ("Ahmet", 85, 90, 78),
    ("Mehmet", 70, 65, 80),
    ("Ayşe", 95, 92, 88)
    ]
sonuc = ogrenci_ortalama_hesapla(ogrenciler)
print(sonuc)