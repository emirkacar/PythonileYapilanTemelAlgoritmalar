
d={}
n = int(input())

for i in range(n):
    data = input()
    d[i]=data

liste = list(d.values())
sozluk = {}

for i in liste:
    if(i not in sozluk):
        sozluk[i] = 1
    else:
        sozluk[i]+=1
z = []
yeniSozluk = {}
yeniListe = []
for k,v in sozluk.items():
    k=k.split()
    for i in k:
        if(i.isdigit()):
            z.append(v*int(i))
            yeniListe.append(int(k[-1])*v)
sozluk_degerlerinin_uzunlugu = len(sozluk.values())
sayac=0
w = []
sozluk_key_listesi = list(sozluk.keys())
sozluk_value_listesi = list(sozluk.values())
string = ""
print()
for i,m in zip(sozluk_key_listesi,yeniListe):
    i = i.split()
    i.pop()
    i.append(m)
    x=[]
    x = i.copy()
    for h in x:
        print(h,end=" ")
    print()
    