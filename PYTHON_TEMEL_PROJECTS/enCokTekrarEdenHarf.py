import string


metin = "Merhaba Dünya!"
temiz_metin = metin.translate(str.maketrans("", "", string.punctuation))

listeye_cevrilmis_hali = list(temiz_metin.lower())
sayac = 0
maks_tekrar_eden_harf = listeye_cevrilmis_hali[0]
for harf in listeye_cevrilmis_hali:
    if(listeye_cevrilmis_hali.count(harf) > listeye_cevrilmis_hali.count(maks_tekrar_eden_harf)):
        maks_tekrar_eden_harf=harf
        sayac+= 1
print([maks_tekrar_eden_harf,listeye_cevrilmis_hali.count(maks_tekrar_eden_harf)])

