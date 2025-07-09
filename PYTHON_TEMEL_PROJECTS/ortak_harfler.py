



def ortakHarfler(metin1,metin2):
    l=[
    ]
    for i in metin1:
        if(i in metin2):
            l.append(i)
    return l

sonuc=ortakHarfler("elma", "limon") 
print(sonuc)




