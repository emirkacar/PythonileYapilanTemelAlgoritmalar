import math

class KesirHesaplayici:
    
    def __init__(self,pay,payda):
        if(payda==0):
            raise ValueError("Payda sifir olamaz.")
        self.pay=pay
        self.payda=payda
      
    def sadelestir(self):
        ebob=math.gcd(self.pay,self.payda)
        self.pay//=ebob
        self.payda//=ebob
    
    def ondalikGoster(self):
        return (f"{self.pay}/{self.payda}")
    
    def topla(self,other):
        yeniPay=self.pay*other.payda+other.pay*self.payda
        yeniPayda=self.payda*other.payda
        return KesirHesaplayici(yeniPay,yeniPayda)
    
    def cikar(self,other):
        yeniPay=self.pay*other.payda-other.pay*self.payda
        yeniPayda=self.payda*other.payda
        return KesirHesaplayici(yeniPay,yeniPayda)

    def carp(self,other):
        yeniPay=self.pay*other.pay
        yeniPayda=self.payda*other.payda
        return KesirHesaplayici(yeniPay,yeniPayda)
    
    def bol(self,other):
        if other.pay == 0:
            raise ValueError("Sifira bölme hatasi.")
        yeniPay=self.pay * other.payda
        yeniPayda=self.payda * other.pay
        return KesirHesaplayici(yeniPay,yeniPayda)
    
    def tersCevir(self):
        if(self.pay==0):
            raise ValueError("Sifirin tersi alinmaz.")
        return KesirHesaplayici(self.payda,self.pay)
    
    def mutlakDeger(self):
        return KesirHesaplayici(abs(self.pay),self.payda)
    
    def tersCevir(self):
        if(self.pay==0):
            raise ValueError("Sifirin tersi alinmaz.Yoksa payda sifir oluyor.")
        return KesirHesaplayici(self.payda, self.pay)
    
    def usAl(self,us):
        if(us>=0):
            yeniPay = self.pay**us
            yeniPayda = self.payda**us
        else:
            if(self.pay==0):
                raise ValueError
            yeniPay=self.payda**abs(us)
            yeniPayda=self.pay**abs(us)
        return KesirHesaplayici(yeniPay,yeniPayda)
    
    def __str__(self):
        return (f"{self.pay}/{self.payda}")


k1=KesirHesaplayici(3,4)
k2=KesirHesaplayici(1,2)


print(f"k1 = {k1}")
print(f"k2 = {k2}")
print(f"k1 + k2 = {k1.topla(k2)}")
print(f"k1 - k2 = {k1.cikar(k2)}")
print(f"k1 * k2 = {k1.carp(k2)}")
print(f"k1 / k2 = {k1.bol(k2)}")

print(f"k1'in tersi = {k1.tersCevir()}")
print(f"|k1| = {k1.mutlakDeger()}")
print(f"k1^2 = {k1.usAl(2)}")