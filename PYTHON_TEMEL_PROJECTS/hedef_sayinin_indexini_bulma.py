
nums = [2,7,11,15]
target=9
d={}
uzunluk = len(nums)

for i in range(uzunluk):
    if(nums[i] not in d):
        d[nums[i]] = i

key_list = list(d.keys())
value_list = list(d.values())

for i in key_list:
    for j in key_list:
        if(i+j == target):
            print(d[i],d[j])
