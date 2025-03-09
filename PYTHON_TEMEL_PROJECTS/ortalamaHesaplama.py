
sinav_sonuclari = {
    "Ali": [80, 90, 85, 75],
    "Ayşe": [95, 92, 88, 91],
    "Mehmet": [70, 72, 68, 75],
    "Zeynep": [88, 85, 92, 91]
}
d = {}
for k,v in sinav_sonuclari.items():
    toplam = 0
    for i in v:
        toplam+=i
    d[k] = toplam//len(v)

en_yuksek_not = d["Ali"]

for k,v in d.items():
    if(en_yuksek_not<v):
        en_yuksek_not = v
        en_yuksek_not_alan_hoca = k

x = []
for ogrenci,sonuc in sinav_sonuclari.items():
    sayac = 0
    for nots in sonuc:
        if(nots>80):
            sayac+=1
    if(sayac==len(sonuc)):
        x.append(ogrenci)


print(d)
print(en_yuksek_not_alan_hoca)
print(sinav_sonuclari["Ayşe"])
print(x)


        
