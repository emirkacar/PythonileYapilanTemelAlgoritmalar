def mukemmelSayi():
    liste = []
    for i in range(1,1000):
        toplam = 0
        for j in range (1,i):
            if(i % j == 0):
                toplam += j
        if(toplam == i):
            liste.append(i)
    return liste







print(mukemmelSayi())
