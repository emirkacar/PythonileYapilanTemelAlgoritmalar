

cumle = input("Bir cumle giriniz: ")
cumle = cumle.split()
n=len(cumle)
for i in range(n):
    cumle[i] = cumle[i].upper()
cumle=cumle[::-1]
donusturulmus_cumle = " ".join(cumle)
print(donusturulmus_cumle)