
liste =  [1, 2, 3, 2, 4, 2, 5, 2]
d = {}

for i in liste:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
valueList = list(d.values())
maksEleman = valueList[0]

for i in valueList:
    if(maksEleman<i):
        maksEleman=i
for k,v in d.items():
    if(v == maksEleman):
        en_buyuk_key = k
print(en_buyuk_key)




    


