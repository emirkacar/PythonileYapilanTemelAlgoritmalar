
l = []
for i in range(1,51):
    l.append(i)
n=len(l)
for i in range(n):
    if(l[i]%3==0):
        if(l[i]%7==0):
            l[i] = "BigBang"
        else:
            l[i] = "Big"
    elif(l[i]%7==0):
        l[i] = "Bang"
    
for i in l:
    print(i)
