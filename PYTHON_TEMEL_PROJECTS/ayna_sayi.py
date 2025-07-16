


sayi = input("Sayi giriniz: ")
orta = len(sayi) // 2
sol_taraf = sayi[:orta]
sag_taraf = sayi[orta:]
sayi3 = sag_taraf[::-1]
if(sol_taraf == sag_taraf or sol_taraf == sayi3):
    print(sayi)