
def swap(liste):
    uzunluk = len(liste)
    i = 0
    j = uzunluk-1
    while(True):
        if(i == j):
            break
        gecici = liste[i]
        liste[i]=liste[j]
        liste[j] = gecici
        i+=1
        j-=1
    print("Listenin son hali:")
    for i in liste:
        print(i,end=" ")
    print()

def f(liste):
    j = 1
    i = 1
    myListe = [10,11,12,13,14,15]
    sayac = 0
    uzunluk = len(liste)
    while(1):
        if(j == uzunluk - 1 and i == uzunluk -1):
            if(sayac == 0):
                sayac+=1
                break
        i+=1
        j+=1
        for i in range(len(myListe)):
            myListe[i]+=10
        
        while(1):
            secim = int(input("Bir secim yapiniz.1'e basarsaniz swap islemi gerceklestirilecektir."))
            if(secim == 1):
                swap(liste)
            else:
                break
        break
liste = [100,200,300,400,500]
f(liste) 