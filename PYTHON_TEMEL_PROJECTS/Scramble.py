
def scramble(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    str2_uzunluk = len(str2)
    sayac=0
    metin = []
    i_nin_sayisi=0
    hedef = list(str2)

    if str2_uzunluk > len(str1):
        return False
    else:
        for i in str2:
            sayac=0
            if(i in str1):
                for j in str1:
                    if(i==j):
                        metin.append(i)
            else:
                return False
    sadelestir = set(hedef)
    sadelestir_str2 = set(str2)
    if(sadelestir==sadelestir_str2):
        return True
    else:
        return False
sonuc = scramble("datascientist","sedat")
print(sonuc)




