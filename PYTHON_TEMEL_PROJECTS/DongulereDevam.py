
#BİR SAYİNİN RAKAMLARİNİN BULUNDUKLARİ KONUMA GORE KUVVETLERİNİN TOPLAMİ SAYİNİN KENDİSİNE ESİTSE BU SAYİYA DİSARİUM SAYİSİ DENİR.KULLANİCİDAN POZİTİF BİR TAM SAYİ ALİN VE BU SAYİNİN DİSARİUM SAYİSİ OLUP OLMADIĞINI BULAN PRORAMI YAZINIZ.

x=input("Bir sayi giriniz:  ")
sayilarinUssu=0
i=0

while(i < 4):
    sayilarinUssu+=int(x[i])**(i+1)
    i+=1

print(sayilarinUssu)
if(int(x)==sayilarinUssu):
    print("disarium")
else:
    print("notdisarium")