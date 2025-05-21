def x(metin):
    l=[]
    for i in metin:
        a = metin.count(i)
        if((i,a) not in l):
            if(i!=' '):
                l.append((i,a))
    return l



sonuc = x("Hello World")
print(sonuc)
