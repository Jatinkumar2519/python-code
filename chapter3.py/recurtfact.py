cube = lambda a :a**3
print(cube(2))




def cube (x):
    return x **3
list1 = [3,4,5,6,7,8]
print(list(map(lambda x:x**3,list1)))
print(list(map(cube,list1)))
print([x**3 for x in list1])
