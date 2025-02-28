
calisanlar = [
    "Ali-IT-10000",
    "Ayşe-HR-12000",
    "Mehmet-IT-11000",
    "Zeynep-Finans-13000",
    "Burak-HR-12500"
]

zam_oranlari = {
    "IT": 0.10,
    "HR": 0.07,
    "Finans": 0.05
}
guncellenmis_liste = []

for calisan in calisanlar:
    calisan,departman,eski_maas = calisan.split("-")
    eski_maas=int(eski_maas)
    if(departman in zam_oranlari):
        yeni_maas = eski_maas + (eski_maas * zam_oranlari[departman])
    else:
        yeni_maas=eski_maas
    guncellenmis_liste.append(f"{calisan},{departman},{int(yeni_maas)}")
for i in guncellenmis_liste:
    print(i)

    
