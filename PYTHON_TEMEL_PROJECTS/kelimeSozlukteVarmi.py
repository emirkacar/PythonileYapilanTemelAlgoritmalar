kelimeSayisi = int(input("Sozlukte kac kelime olucak: "))
d = {}

for i in range(kelimeSayisi):
    kelimeniz = input("Kelime(Ingilizce-Turkce): ")
    kelimeniz = kelimeniz.split(" ")
    if(len(kelimeniz)==2):
        d.update({kelimeniz[0]:kelimeniz[1]})
    else:
        print("Hatali giris! Kelimeyi su formatta girin: 'Turkce Ingilizce'")
        i+=1


while(1):
    secim = int(input("0-2 arasinda bir secim yapiniz. -1(Program sonlanir) "))
    if(secim==-1):
        break
    elif(secim==0):
        kelimeCifti = input("Please,enter a english word: ")
        kelimeCifti = kelimeCifti.split(" ")
        if(len(kelimeCifti)==2): 
            if(kelimeCifti[0] not in d):
                print(f"{kelimeCifti[0]} bulunamadi")
            else:
                print(kelimeCifti[1])
    elif(secim==1):
        kelimeCifti = input("Please,enter a Turkish and English word")
        kelimeCifti = kelimeCifti.split(" ")
        if(len(kelimeCifti)==2): 
            if(kelimeCifti[0] not in d):
                d.update({kelimeCifti[0]:kelimeCifti[1]})
        print(d)

        

            