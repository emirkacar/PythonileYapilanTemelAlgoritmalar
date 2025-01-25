
set1 = {1, "python", 2, "java", 3, "hello"}
l = list(set1)
numListesi = []

for i in l:
    if(str(i).isdigit()):
        numListesi.append(int(i))
s = set(numListesi)
print(s)
print(set1-s)


