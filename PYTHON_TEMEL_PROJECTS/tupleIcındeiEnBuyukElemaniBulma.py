
def f(l):
    differentMaks_list = []
    enbuyukIkinciElemanListesi = []

    for i in l:
        maks = i[0]
        for j in i:
            if(maks<j):
                maks=j
        differentMaks_list.append(maks)
    for tup in l:
        maks = tup[0]
        for deger in tup:
            if(deger not in differentMaks_list and maks<deger):
                maks=deger
                enbuyukIkinciElemanListesi.append(maks)
    return enbuyukIkinciElemanListesi
tuple_listesi = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
sonuc = f(tuple_listesi)
print(sonuc)