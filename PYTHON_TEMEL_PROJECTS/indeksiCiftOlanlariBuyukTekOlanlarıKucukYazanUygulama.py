
string = "hi my name is john and i am learning python"
newString = ""  

for i in range(len(string)):
    if(i % 2 == 0):
        newString += string[i].upper()
    else:
        newString += string[i]
print(newString)


