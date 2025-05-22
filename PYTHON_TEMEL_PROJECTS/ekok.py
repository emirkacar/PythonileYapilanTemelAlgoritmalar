


liste = [10, 9, 2, 5, 3, 7, 101, 18]

gecerli=[]
en_uzun = []
n=len(liste)
for i in range(1,n):
    if(liste[i-1] > liste[i]):
        konum = liste.index(liste[i-1])
        gecerli = [konum+i:]

    gecerli.append(i)
    if(len(gecerli) > len(en_uzun)):
        en_uzun=gecerli
print(en_uzun)

