globalVeri = ""
globalSozluk={}

def fonksiyon():
    global globalVeri
    globalVeri = input("Veri giriniz: ")
    ayir(globalVeri)

def ayir(veri):
    global globalVeri
    globalVeri=veri.lower().split()
    print(globalVeri)
    gruplandir(globalVeri)

def gruplandir(veri):
    global globalSozluk
    globalSozluk = {}

    for kelime in veri:
        uzunluk = len(kelime)
        anahtar = f"{uzunluk} harfli kelimeler"
        if(anahtar not in globalSozluk):
            globalSozluk[anahtar]=[]
        globalSozluk[anahtar].append(kelime)
    ekranaYazdir(globalSozluk)


def ekranaYazdir(veri):
    for k,v in veri.items():
        print(k,v)

main=True
while(True):
        if(main):
            print("""
            1-Kullanicidan metin girmesini iste
            2-Metni kelimelere ayir ve her kelimeyi kucuk harfe cevir
            3-Kelimeleri uzunluklarina gore gruplandir.
            4-Gruplandirilmis kelimeleri ekrana yazdir
            5-Menuyu listele
            6-Cikis""")
            secim=int(input("1-6 arasi bir secim yapiniz: "))
            if(secim==1):
                fonksiyon()
            elif(secim==2):
                ayir()
            elif(secim==3):
                gruplandir()
            elif(secim==4):
                ekranaYazdir()
            elif(secim==5):
                main=True
            elif(secim==6):
                break
            else:
                print("1-6 arasi secim yapiniz")
                
        main=False