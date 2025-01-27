

liste = [1, -2, 3, 5, -1, 2]
liste_uzunlugu = len(liste)
d = {}

for i in range(liste_uzunlugu):
    altListeler = []
    for j in range(i,liste_uzunlugu):
        altListeler.insert(i,liste[j])
        if(len(altListeler)==2):
            d[i] = altListeler
            break
sozluk_values = list(d.values())
toplam_sozlugu = {}

for i in sozluk_values:
    toplam_sozlugu[(tuple(i))]=sum(i)
print(toplam_sozlugu)

toplam_sozlugu_keys_liste = list(toplam_sozlugu.keys())
maksimum_toplam = max(toplam_sozlugu.values()),
print(toplam_sozlugu.items())
maksimum_ikili = max(toplam_sozlugu.items(),key=lambda x:x[1])
print(f"Maksimum toplam {maksimum_toplam}")
print(f"Bu toplami veren ikili {maksimum_ikili} ")
print(toplam_sozlugu.items())