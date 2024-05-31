#Listenin tersini alma 
def tersiniAl(liste):
    listeninTersi = []
    for i in range(len(liste) -1 ,-1,-1):
        listeninTersi.append(liste[i])
    return listeninTersi


liste = [3,6,9,100,-5,14]
print(tersiniAl(liste))