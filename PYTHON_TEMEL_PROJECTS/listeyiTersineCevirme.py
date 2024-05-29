def ters(liste):
    uzunluk = len(liste)
    for i in range(uzunluk//2):
        gecici = liste[i]
        liste[i]=liste[uzunluk-1-i]
        liste[uzunluk-1-i] = gecici
        
    return liste




liste = [1,2,3,4,5,6,7,8,9,10]
print(ters(liste))