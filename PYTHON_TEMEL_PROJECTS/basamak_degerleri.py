
sayi =input("Sayi: ")
l = []
basamak_degerleri = 1
if(sayi[0] == '-'):
    deger = int(sayi[1:])    
else:
    deger = int(sayi)

while(deger>0):
    if len(str(deger)) ==1:
        if(deger<0):
            deger = deger  * -1
            l.append(deger)
        else:
            deger=basamak_degerleri*deger
            l.append(deger)
        break
            
    if(deger<0):
        birler=(deger %10) * -1
    else:
        birler=(deger%10) 
    l.append(birler*basamak_degerleri)
    deger//=10
    basamak_degerleri = basamak_degerleri*10

l.reverse()

if(sayi[0] == '-'):
    n=len(l)
    for i in range(n):
        l[i] = l[i] * -1
print(l)

