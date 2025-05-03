



l = [1,2,3,1,2,1,3,4]
n = len(l)
new_list = []
d = {}
for i in range(n):
    if(l[i] not in d):
        d[l[i]] = 1
    else:
        d[l[i]] += 1
list_keys = list(d.keys())
print(list_keys)
