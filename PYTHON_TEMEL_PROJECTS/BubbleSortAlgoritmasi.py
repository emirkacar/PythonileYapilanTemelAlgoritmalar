#Bubble Sort Algoritmasi
liste = [10,150,122,1,-100]

for i in range(len(liste)):
    for j in range(0,len(liste)-1-i):
        if ( liste[j] > liste[j+1] ):
            gecici = liste[j]
            liste[j] = liste[j+1]
            liste[j+1] = gecici
print(liste)








