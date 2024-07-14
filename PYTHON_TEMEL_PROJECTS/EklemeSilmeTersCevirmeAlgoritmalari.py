#Append metodunu kullanmadan diziye eleman ekleme algoritmasi.
from array import *

n = int(input("Diziye kac eleman ekleyeceksiniz: "))
arr = array('i',[])


for i in range(n):
    sayi=int(input("Sayi: "))
    arr += array('i',[sayi])
print(arr)


#Remove metodunu gerceklestirmeden diziden eleman cikarma algoritmasi.
#5 degerlerini sil.

silinmisDizi = array('i',[])
for index,sayi in enumerate(arr):
    if(sayi != 5):
        silinmisDizi += array('i',[sayi])
arr = silinmisDizi
        
print(arr)


#reverse metodunu kullanmadan dizi elemanlarini ters cevirme algoritmasi
tersDizi = array('i',[])

for i in range(len(arr)-1,-1,-1):
    tersDizi += array('i',[arr[i]])
arr = tersDizi
print(arr)
















