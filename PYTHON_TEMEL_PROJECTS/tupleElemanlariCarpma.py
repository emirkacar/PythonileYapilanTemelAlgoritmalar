def f(l):
    carpimListesi = []
    for i in l:
        carpim = 1
        for j in i:
            if(str(j).isdigit()):
                carpim*=int(j)
        carpimListesi.append(carpim)
    return carpimListesi 


tuple_listesi = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
sonuc = f(tuple_listesi)
print(sonuc)
