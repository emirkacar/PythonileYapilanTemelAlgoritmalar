
metin = "Pythooon programlama dili çok güçlüdür!"
metin = metin.split()
d = {}
n = len(metin)

for i in range(n):
    metin[i] = metin[i].replace("!","")

for i in range(n):
    max_index = i
    for j in range(i+1,n):
        if(len(metin[j]) > len(metin[max_index])):
            max_index = j
    metin[max_index],metin[i] = metin[i],metin[max_index]
print(metin)

for i in metin:
    for j in i:
        if(j not in d):
            d[j] = 1
        else:
            d[j] += 1
max_deger = max(d,key=lambda x:d[x])
print(f"En cok tekrar eden harf : {max_deger} , tekrar sayisi : {d[max_deger]}")

