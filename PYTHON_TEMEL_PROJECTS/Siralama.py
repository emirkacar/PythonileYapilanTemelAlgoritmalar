sayi1=input("Sayi1: ")
sayi2=input("Sayi2: ")
sayi3=input("Sayi3: ")
bool = True

if(sayi1.isdigit() and sayi2.isdigit() and sayi3.isdigit()):
    if(sayi1>sayi2 and sayi1<sayi3):
        print(bool)
    else:
        bool=False
        print(bool)
else:
    bool=False
    print(bool)
    
    
    