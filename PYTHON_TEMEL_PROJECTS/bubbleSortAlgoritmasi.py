def algoritma(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if(liste[j]>liste[j+1]):
                gecici = liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=gecici
            print(liste)
    
    
liste=[21,13,9,12,4]
print(algoritma(liste))