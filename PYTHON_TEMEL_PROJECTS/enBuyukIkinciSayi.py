

def en_buyuk_ikinci_eleman(liste):
    if(len(liste)<2):
        return "Listede en az 2 eleman olmali."
    maks_eleman=liste[0]
    for eleman in liste:
        if(maks_eleman<eleman):
            maks_eleman=eleman
    maks_ikinci_eleman = liste[0]
    for eleman in liste:
        if(maks_eleman > maks_ikinci_eleman and maks_ikinci_eleman < eleman and eleman < maks_eleman):
            maks_ikinci_eleman=eleman
    return maks_ikinci_eleman
        

liste = [10, 20,4, 45, 99, 99]           
enB=en_buyuk_ikinci_eleman(liste)
print(enB)
































