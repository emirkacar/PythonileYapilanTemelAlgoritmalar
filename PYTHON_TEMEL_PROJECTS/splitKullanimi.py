

l = [
    "Emir-Kacar",
]
new_list = []
for i in l:
    ad,soyad=i.split("-")
    new_list.append(f"{ad} {soyad}")
for i in new_list:
    print(i)



    
