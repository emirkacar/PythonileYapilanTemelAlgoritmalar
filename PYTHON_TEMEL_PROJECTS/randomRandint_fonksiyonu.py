import random 

l=[]
sayac=0
while(True):
    if(sayac==7):
        break
    i=random.randint(1,36)
    l.append(i)
    sayac+=1    
print(l)

toplam = 0
for i in l:
    toplam+=i
print(toplam/7)
