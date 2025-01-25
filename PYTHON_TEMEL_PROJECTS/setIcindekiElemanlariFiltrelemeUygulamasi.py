


set1 = {10, 20, 30, 40, 50, 60, 70}
l = list(set1)

enBuyukUcEleman = []
sayacB=0

sayacK =0
enKucukUcEleman = []

while(sayacB < 3):
    maksEleman = float('-inf') 
    for i in l:
        if(maksEleman<i):
            maksEleman=i
    enBuyukUcEleman.append(maksEleman)
    l.remove(maksEleman)
    sayacB+=1   
print(set(enBuyukUcEleman))
        
while(sayacK<3):
    minEleman = float('inf') 
    for i in l:
        if(minEleman > i):
            minEleman=i
    enKucukUcEleman.append(minEleman)
    l.remove(minEleman)
    sayacK+=1
print(set(enKucukUcEleman))



