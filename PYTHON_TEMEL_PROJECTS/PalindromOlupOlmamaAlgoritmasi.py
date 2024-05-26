
while (True):
    kelime = input("Bir kelime giriniz: ")
    palindrome=True
    for i in range(len(kelime)):
        if(kelime[i]!= kelime[-i-1]):
            palindrome=False
            break
    if(palindrome):
        print("Kelime palindromedur.")
        break
        
    else:
        print("Kelime palindrom degildir.")
        break