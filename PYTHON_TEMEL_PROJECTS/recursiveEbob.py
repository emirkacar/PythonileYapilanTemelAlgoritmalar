
def ebob(sayi1,sayi2):
    remainder = 0
    if(sayi2==0):
        return sayi1
    else:
        remainder=sayi1%sayi2
        return ebob(sayi2,remainder)


sayi1=int(input("Sayi1: "))
sayi2=int(input("Sayi2: "))

print(ebob(sayi1,sayi2))




















