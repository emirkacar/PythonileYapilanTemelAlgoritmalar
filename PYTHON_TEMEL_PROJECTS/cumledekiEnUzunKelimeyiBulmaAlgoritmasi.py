

cumle = "Python programlama dili harika"
cumle = cumle.split()

maks_uzun_olan_kelime = cumle[-1]

for i in cumle:
    if(len(i) > len(maks_uzun_olan_kelime)):
        maks_uzun_olan_kelime=i
print(f"{cumle} listesindeki en uzun kelime = {maks_uzun_olan_kelime}")

