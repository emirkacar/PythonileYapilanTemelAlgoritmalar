s = "abc123xyz45"

toplam = 0
for i in s:
    if(i.isdigit()):
        toplam+=int(i)
print(toplam)