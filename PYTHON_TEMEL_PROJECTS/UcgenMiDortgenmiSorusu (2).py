#UCGEN Mİ DORTGEN Mİ OLDUGUNU BULAN ALGORİTMA SORUSU

tip=input("Lutfen ucgen mi dortgen mi oldugunu giriniz  ")

if(tip=="Dortgen"):
    kenar1=int(input("1.kenari giriniz."))
    kenar2=int(input("2.kenari giriniz."))
    kenar3=int(input("3.kenari giriniz."))
    kenar4=int(input("4.kenari giriniz."))

    if(kenar1==kenar2==kenar3==kenar4):
        print("Tip = kare")
    elif (kenar1==kenar2 or kenar3==kenar4 ):
        print("Tip = dikdortgen ")
    elif ( kenar1==kenar3 or kenar2==kenar4):
        print("Tip = Dikdortgen")
    elif ( kenar1==kenar4 or kenar2==kenar3):
        print("Tip==Dikdortgen ")
if(tip=="Ucgen"):
    x=int(input("x'in kenar uzunlugu : "))
    y=int(input("y'nin kenar uzunlugu : "))
    z=int(input("z'nin kenar uzunlugu : "))
    if(x==y and x==z):
        print("Eskenar ucgen")
    elif (x==y and x!=z):
        print("Ikizkenar ucgen")
    elif (x!=y and y!=z):
        print("Cesitkenar ucgen.")
    else:
        print("Ucgen belirtmiyor.")






