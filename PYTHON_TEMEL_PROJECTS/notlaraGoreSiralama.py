


notlar = {"Ali": 85, "Mehmet": 92, "Zeynep": 78, "Elif": 95, "Burak": 88}
notlar_keys = list(notlar.keys())
notlarValues = list(notlar.values())
l = []
d = {}
sozluk = {}
n = len(notlarValues)

for i in range(n):
    max_index = i
    for j in range(i+1,n):
        if(notlarValues[j] > notlarValues[max_index]):
            max_index=j
    notlarValues[i] , notlarValues[max_index] = notlarValues[max_index] , notlarValues[i]
    notlar_keys[i] , notlar_keys[max_index] = notlar_keys[max_index],notlar_keys[i]
for i in range(n):
    d[notlar_keys[i]] = notlarValues[i]
print(d)


            






