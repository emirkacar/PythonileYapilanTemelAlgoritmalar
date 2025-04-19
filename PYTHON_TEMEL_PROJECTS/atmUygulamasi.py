
bakiye = 500
kart_sifre = 1234
sayac = 3
for i in range(3):
    sifre_gir = int(input("Sifrenizi giriniz: "))
    if(sayac==0):
        print("Kartiniz bloke edilmistir...")
        break
    if(kart_sifre==sifre_gir):    
        while(1):
            print("""
                ATM'YE HOSGELDINIZ.
                1-PARA CEKME
                2-PARA YATIRMA
                3-BAKİYE SORGULAMA
                4-KART IADE
                5-CIKIS""")
            secim=int(input("1-5 arasi bir secim yapiniz: "))
            if(secim in [1,2,3,4,5]):
                if(secim==1):
                    cekilecek_miktar = int(input("Kac TL cekeceksiniz? "))
                    if(cekilecek_miktar>bakiye):
                        print("Bakiye yetersiz...")
                        continue
                    else:
                        bakiye -= cekilecek_miktar
                    print(f"Hesabinizdan {cekilecek_miktar} TL cekilmistir.Kalan Tutar = {bakiye}")
                elif(secim==2):
                    yatiralacak_para=int(input("Ne kadar yatiracaksiniz? "))
                    if(yatiralacak_para>bakiye):
                        print("Bakiyeniz yetersiz")
                    else:
                        bakiye+=yatiralacak_para
                        print(f"{yatiralacak_para} TL yatirilmistir.Mevcut bakiye = {bakiye}")
                elif(secim==3):
                    print("Bakiyeniz goruntuleniyor...")
                    print(bakiye)
                elif(secim==4):
                    print("Kartiniz iade ediliyor.")
                else:
                    print("Cikis yapiliyor...")
                    exit()
            else:
                print("Yanlis secim yaptiniz tekrar deneyiniz.")
                secim=input("Devam etmek istiyor musunuz?(e-h) ").lower()
                if(secim=="e"):
                    continue
                else:
                    break
    else:
        sayac-= 1
        print(f"Kalan giris hakkiniz = {sayac}")
        if(sayac==0):
            print("Kartiniz bloke edilmistir...")
            break
