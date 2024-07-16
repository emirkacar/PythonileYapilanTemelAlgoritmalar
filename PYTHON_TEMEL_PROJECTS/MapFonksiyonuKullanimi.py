


liste = [(3,4),(10,3),(5,6),(1,9)]
newList = []
def alanHesapla(sayiCifti):
    newList.append(sayiCifti[0]*sayiCifti[1])

list(map(alanHesapla,liste))
print(newList)











