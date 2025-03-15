

metin = "Python ile algoritma geliştirmek çok eğlenceli"
metin = metin.split()
n = len(metin)

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if(len(metin[j]) < len(metin[min_index])):
            min_index = j
    metin[min_index] , metin[i] = metin[i] , metin[min_index]
print(metin)

