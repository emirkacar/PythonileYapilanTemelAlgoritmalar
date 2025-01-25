
liste = [1, 2, 2, 3, 4, 4, 4, 5]
d={}
s = set(liste)
l = []
for i in liste:
    if(i not in d):
        d[i] = 1
    else:
        d[i]+=1
print(f"Frekans sozlugu = {d}")
for k,v in d.items():
    if(v>1):
        l.append(k)
print(f"Tekrar eden elemanlar = {set(l)}")

        











