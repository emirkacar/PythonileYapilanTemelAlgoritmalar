


satir = int(input("Satir: "))
sutun = int(input("Sutun: "))

a=[]

for i in range(satir):
    x=[]
    for j in range(sutun):
        eleman = int(input(f"a[{i}][{j}]: "))
        x.append(eleman)
    a.append(x)
transpose =[]

for i in range(satir):
    p =[]
    for j in range(sutun):
        p.append(0)
    transpose.append(p)


    
for i in range(satir):
    for j in range(sutun):
        transpose[i][j] = a[j][i]

for i in range(satir):
    for j in range(sutun):
        print(transpose[i][j],end=" ")
    print()