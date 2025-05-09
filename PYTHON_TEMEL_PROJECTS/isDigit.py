
deger = input("Deger: ")
x = ""
n=len(deger)
if(deger.isdigit()):
    for i in deger:
        if(int(i)<=3):
            x += str(int(i)**2)
        elif(int(i)>=3):
            if(int(i) %2==0):
                x+=str(int(i)+1)
            else:
                x+=str(int(i)-2)
   
else:
    print("invalid input")
print(x)


