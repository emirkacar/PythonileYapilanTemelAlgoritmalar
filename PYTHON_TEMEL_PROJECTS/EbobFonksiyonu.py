def ebobFunction(x,y):
    if(x == y):
        ebob = y
    elif (x>y):
        bolen = y
        while(bolen != 0):
            if(x % bolen ==0 and y % bolen == 0):
                ebob = bolen
                break
            bolen-=1
    else:
        bolen = x
        while(bolen != 0):
            if(y % bolen == 0 and x % bolen == 0):
                ebob = bolen
                break
            bolen-=1
    return ebob

sayi1 = int(input("Sayi1 : "))
sayi2=int(input("Sayi2 : "))

sonuc = ebobFunction(sayi1,sayi2)   
print("Iki sayinin ebobu = ",sonuc)