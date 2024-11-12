def championship(takimSayisi):
    takimlar = []
    sampiyonluklar = []
    yildizlar = []

    for i in range(takimSayisi):
        takimIsmi = input("Takim ismini giriniz: ")
        sampiyonlukSayisi=int(input("Takim kac kere sampiyon oldu? "))
        takimlar.append(takimIsmi)
        sampiyonluklar.append(sampiyonlukSayisi)
        yildizlar.append((sampiyonlukSayisi//7)*'*')
    print(f"{"Takim Adi":<20}{"Şampiyonluk Sayisi":<20}{"Yildizlar"}")
    for i,j,k in zip(takimlar,sampiyonluklar,yildizlar):
        print(f"{i:<20}{j:<20}{k}")

takimSayisi = int(input("Takim sayisini giriniz: "))
championship(takimSayisi)