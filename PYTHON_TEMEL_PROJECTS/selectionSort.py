L = [12,23,7,-8,10,6,16,7,7,9]
print("Orijinal hali:")
print(L)
print()

print("Degisiklik sonrasi:")


for i in range (len(L)):
    for j in range (len(L)-1):
        if (L[j+1] < L[j]):
            gecici = L[j+1]
            L[j+1] = L[j]
            L[j] = gecici
print(L)
