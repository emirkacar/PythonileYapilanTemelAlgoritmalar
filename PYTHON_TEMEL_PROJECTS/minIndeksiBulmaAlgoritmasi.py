#Listedeki en kucuk sayinin indeksini bulma algoritmasi(Ic ice döngü ile)

liste = [15,6,3,1,100]
minIndex = 0
for i in range(len(liste)):
    for j in range(len(liste)-1):
        if (liste[j] < liste[j+1]):
            minIndex = j
print(minIndex)





#Listedeki en kucuk sayinin indeksini bulma algoritmasi(Tek dongu ile)
liste = [15,6,3,1,100]
minIndex = 0

for i in range(len(liste)-1):
    if(liste[i] < liste[i+1]):
        minIndex = i
print(minIndex)


