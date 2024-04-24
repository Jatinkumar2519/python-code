list1 = list(map(int,input().split()))
print("length:",len(list1))
print("max:",max(list1))
print("min:",min(list1))
print("sum of elements:",sum(list1))
print("enumerate:",list(enumerate(list1)))
print(all([True, " ", 12]))
print(any([True, False]))
print(any([False,False]))
print("sorted list:",sorted(list1))




#list method
list1.append([4,6])
print(list1)
list2 = [12,14]
list1.extend(list2)
print(list1)
list3 = list1.copy()
print(list3)
list1.reverse()
print(list1)
list1.remove(12)
list1.pop()
list1.pop(0)
list1.insert(1, "hello")
print(list1.count(14))
      