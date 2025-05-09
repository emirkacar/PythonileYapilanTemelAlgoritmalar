
sayi = int(input("Sayi: "))
x = []
y=[]
toplam=0
for i in range(1,sayi):
    if(sayi%i==0):
        x.append(i)
        toplam+=i

for i in range(1,toplam):
    if(toplam%i==0):
        y.append(i)
if(sum(y) == sayi):
    print(f"{sayi} ve {toplam} sayilari amicabledir")
else:
    print("Degildir.")




