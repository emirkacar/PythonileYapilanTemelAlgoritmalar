
def divide_students(students):
    grup = [[],[]]
    for i,student in enumerate(students):
        if ( i % 2 == 0):
            grup[0].append(student)
        else:
            grup[1].append(student)
    return grup
        

students = ["John","Mark","Venessa","Mariam"]

print(divide_students(students))



