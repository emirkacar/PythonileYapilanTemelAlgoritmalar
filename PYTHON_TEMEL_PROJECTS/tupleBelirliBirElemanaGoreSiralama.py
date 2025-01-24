
def f(l):
    toplam = 0
    d={}
    sayac = 0
    for i in l:
        toplam=0
        for j in i:
            if(str(j).isdigit()):
                toplam+=int(j)       
        d[i]=toplam//3
        sayac += 1
    return max(d)
ogrenci_listesi = [("Ali", 85, 20), ("Veli", 90, 21), ("Ayşe", 80, 19)]
print(f(ogrenci_listesi))