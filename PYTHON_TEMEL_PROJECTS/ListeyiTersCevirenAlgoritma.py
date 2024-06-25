def enBuyukEleman(liste):

    for i in range(len(liste)//2):
        gecici = liste[i]
        liste[i] = liste[len(liste)-1-i]
        liste[len(liste)-1-i] = gecici
    return liste


liste = [100,50,20,106,12,14,16,13,650,29,28,14,6,0,-5,129,-3]

print(enBuyukEleman(liste))

