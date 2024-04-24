

a = [1,2,3,4,5,6]
b = [1,3,4,6,7,8]

print(list(filter(lambda x : x in a ,b)))
print(list(filter(lambda x : x in a , b)))
print([x for x in a if x in b])