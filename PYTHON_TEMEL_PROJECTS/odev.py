#1.Soru
def duzlestir(liste):
    duzListe = []
    def listeninIciniDuzlestir(liste):
        for i in liste:
            if ( type(i) == list):
                listeninIciniDuzlestir(i)
            else:
                duzListe.append(i)
    listeninIciniDuzlestir(liste)
    return duzListe






girdi = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
sonuc = duzlestir(girdi)
print(sonuc)



#2.Soru

def tersineDondur(girdi):
    a = []
    girdi.reverse()

    for a in girdi:
        a.reverse()
    print(girdi)
    
        
    



girdi =[[1, 2], [3, 4], [5, 6, 7]]
sonuc = tersineDondur(girdi)
print(sonuc)
