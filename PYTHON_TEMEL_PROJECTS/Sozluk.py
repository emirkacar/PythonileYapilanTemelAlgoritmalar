#Sozluk kullanimi ile ogrencinin bilgisini sorgulama programi
ogrenciler = {101:
          {
              "Ad":"Yigit Bilgi",
              "Yas" : 2010,
              "Notlar": (40,80,90)
          },
        102:
        {

            "Ad":"Ada Bilgi",
            "Yas" : 2012,
            "Notlar": (80,80,90)
        },
        103:
        {
            "Ad":"Cinar Turan",
            "Yas" : 2017,
            "Notlar": (70,70,70)
        }

}
ogrenciNo =int(input("Bir ogrenci numarasi giriniz (101,102,103) : "))

if ogrenciNo in ogrenciler:
    ogrenci = ogrenciler[ogrenciNo]
    ad = ogrenci["Ad"]
    yas = 2024 - ogrenci["Yas"]
    notlar = ogrenci["Notlar"]
    ortalama = sum(notlar)/len(notlar)
    
    print(f"{ogrenciNo} numarali {ad} ismindeki ogrencinin yasi {yas} ve not ortalamasi {ortalama}.")
else:
    print("Bu numarali bir ogrenci bulunmamaktadir.")





