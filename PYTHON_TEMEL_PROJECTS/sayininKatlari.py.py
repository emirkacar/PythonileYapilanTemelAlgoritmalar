
sayi = int(input("Sayi giriniz: "))
sayac = 0
i=1
l = []

while(sayi!=0):
    if(sayi%17==0):
        l.append(sayi)
    sayi-=1
n=len(l)
for i in range(n):
    print(l[i]," ",end=" ")
    if(i==10):
        print()
   

    
    