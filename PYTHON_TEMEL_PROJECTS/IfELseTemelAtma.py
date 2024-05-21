""" x=[1,2,3,4,50]

x.append(150)   #listenin sonuna 50 ekledim
print(x)

x.insert(0,3)     #0.karaktere 3'u atadim.
print(x) """





""" x="Emir"
for i in range(0,len(x)):
    print(x[i])"""




""" liste = []
n = int(input("n: " ))


for i in range(n):
    sayi=int(input("sayi: "))
    liste.append(sayi)

for j in range(len(liste)):
    print(liste[j],end=' ') """






""" a=3
b=4
print("{} + {} ' nin sonucu {}'dir.".format(a,b,a+b)) """




""" for i in range(1,11):
    for j in range (1,11):
        print("{} x {} = {}".format(i,j,i*j)) """





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






