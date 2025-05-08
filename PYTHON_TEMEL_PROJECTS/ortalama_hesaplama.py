
liste=[]
for i in range(3):
    veri = input().split()
    ad=veri[0]
    not1,not2,not3 = map(int,veri[1:4])
    liste.append([ad, not1, not2, not3])
ortalama_listesi = []
n = len(liste)

for i in range(n):
    toplam=0
    for j in range(1,len(liste[i])):
        toplam+=liste[i][j]
    ortalama = toplam/3
    ortalama_listesi.append(ortalama)
print(ortalama_listesi)

d = {}
ortalama_listesi_uzunluk = len(ortalama_listesi)
for i in range(ortalama_listesi_uzunluk):
    for j in range(1):
        d[liste[i][0]] = ortalama_listesi[i]
print(d)

for k,v in d.items():
    if(v>=60):
        print(f"{k} ogrencisi {v} ortalamasiyla dersi gecmistir")
    else:
        print(f"{k} ogrencisi {v} ortalamasiyla dersi gecememistir.")
