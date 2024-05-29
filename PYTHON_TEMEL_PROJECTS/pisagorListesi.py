
def pisagor():
    pisagorListesi = []
    for i in range (1,101):
        for j in range (i,101):
            for z in range (j,101):
                if ( i**2 + j**2 == z**2):
                    pisagorListesi.append((i,j,z))
    return pisagorListesi

        
sonuc = pisagor()
print("Pisagor ucgeni olusturanlar = ",sonuc)

