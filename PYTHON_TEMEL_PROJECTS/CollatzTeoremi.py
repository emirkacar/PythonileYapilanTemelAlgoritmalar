
sayi=int(input("Sayi: "))
sayac=0

while(sayi!=1):
    if(sayi%2==0):
        sayi/=2
        print(int(sayi),end=" ")
    else:
        sayi=(sayi*3)+1
        print(int(sayi),end=" ")
    sayac+=1

if(sayi==1):
    print()
    print(sayac)


