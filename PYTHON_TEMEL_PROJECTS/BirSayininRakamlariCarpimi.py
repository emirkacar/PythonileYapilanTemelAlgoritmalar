

num=int(input("Num: "))
carpim = 1
gecici = num

while(gecici!=0):
    kalan=gecici%10
    gecici//=10
    carpim *= kalan

print(f"{num} sayisinin rakamlari carpimi = {carpim}")
