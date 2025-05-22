
def ekok(num1,num2):
    
    i = max(num1,num2)
    while(True):
        if(i%num1==0 and i%num2==0):
            return i
        i+=1


    



sonuc=ekok(4,6)
print(sonuc)