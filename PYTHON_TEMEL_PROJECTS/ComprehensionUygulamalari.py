

#Comprehension Uygulamalari

numbers = range(10)


newDict = {i:i**2 if(i%2==0) else i for i in numbers}
print(newDict)

values = ["total","speeding","alcohol","not.distracted","no_previous","ins_premium","ins_losses","abbrev"]

afterValues = ["FLAG"+i if("ins" in i) else i+"NO_FLAG" for i in values ]
print(afterValues)

