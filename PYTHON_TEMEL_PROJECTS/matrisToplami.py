
satir=int(input("Satir: "))
sutun=int(input("Sutun: "))
a = []
b=[]

for i in range(satir):
    x=[]
    for j in range(sutun):
        eleman =int(input(f"a[{i}][{j}]: "))
        x.append(eleman)
    a.append(x)
for i in range(satir):
    x=[]
    for j in range(sutun):
        eleman =int(input(f"b[{i}][{j}]: "))
        x.append(eleman)
    b.append(x)
toplam_listesi = []
a_uzunluk = len(a)
b_uzunluk = len(b)

for i in range(a_uzunluk):
    for j in range(b_uzunluk):
        toplam_listesi.append(a[i][j] +b[i][j])
print(toplam_listesi)
