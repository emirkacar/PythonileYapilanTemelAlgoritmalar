
import string

def remove_punctuation(metin):
    return metin.translate(str.maketrans('', '', string.punctuation))

metin = "Merhaba! Nasilsin? Merhaba, nasilsin?"
metin = metin.lower()
metin = remove_punctuation(metin)
d = {}
metin = metin.split()
for i in metin:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(f"Kelime frekanslari = {d}")




    