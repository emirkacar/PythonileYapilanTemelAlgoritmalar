def x(l1,l2):
    l1_n = len(l1)
    l2_n=len(l2)
    new=[]
    p = [ l1[i] for i in range(l1_n) for j in range(l2_n) if(l1[i] in l2[j] )]

    p = set(p)
    p=list(p)
    return p

list1=["old","int","age","and"]
list2=["random","soldier","list","introduction","print"]
sonuc=x(list1,list2)
print(sonuc)