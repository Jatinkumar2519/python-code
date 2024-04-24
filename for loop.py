# n = int(input("n: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()




# matrix = [[1,2,3,4] ,[5,6,7,8],[2,3,4,5]]
# transposed = []
# print("matrix:",matrix)
# for i in range(len(matrix[0])):
#     transposed_row = []
#     for row in matrix:
#         print(row)
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)    
# print("transposed",transposed)  




# n = int(input("n: "))
# factors = [1]
# for i in range(2,int(n**0.5 + 1)):
#     if(n%i==0):
#         factors.append(i)
#         if n //i != i:
#             factors.append(n//i)
# print("factors:",sorted(factors))            
# if(sum(factors) == n):
#         print("perfect number")
# else:
#         print("not a perfect number")        
        




# # for i in range(1,21):
# #         if i == 10:
#               break
#         print("*")
        
# num = int(input("num: "))
# digit = []
# sum = 0
# temp = num
# while(temp != 0):
#       digit.append(temp% 10)
#       temp= temp // 10
# for i in digit:
#       sum = sum + i**(len(str(num)))    
#       if(sum == num):

#             print("angastrome no")






# num = int(input("num: "))            
# digit =[]
# temp = num 
# while (num):
#       digit.append(len(str(num)))
#       for i in digit:
#             if i <= digit:
#                   fact = fact * i
                  # i = i + 1




# n = int(input("n:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#         i = i + 1

#     print( )  




# import calendar
# year = 2004
# month = 8
# print(calendar.month(year,month))




# n = int(input("n: "))
# for i in range(0,n+1):
#     print(" " * (n-i-1), end = " ")
#     print(i * (2*i+1), end = " ")
#     print(" " * (n-i-1))
#     i = i +1
# # print()
                

# x = int(input("x: "))
# for i in range(x//2+2):
#     for j in range(x):
#         if 
#         print("*",end = " ")
#     print()

# from math import factorial
# x = int(input("x: "))
# w = str(x)
# list = []
# list1 = []
# for i in range(len(w)):
#     y = w[i]
#     list.append(int(y))
# print(list)
# for i in range(len(list)):
#     s = factorial(list[i])
#     list1.append(int(s))
# print(list1)
# if sum(tuple(list1)) == x:
#     print("strong number")
# else:
#     print("not strong number")

# x = int(input("x: "))
# list = [1]
# for i in range(2,x):
#     if x % i == 0:
#         list.append(i)
# print(list)

# if sum(list) == x:
#     print("perfect number")
# else:
#     print("not a perfect number")


# x = int(input("x: "))
# w = str(x)
# list = []
# for i in range(len(w)):
#     y = w[i]
#     list.append(int(y))
# print(list)
# list1 = []
# for i in range(len(list)):
#     s = list[i]**len(w)
#     list1.append(int(s))
# print(list1)
# if sum(list1) == x:
#     print("angestrom number")
# else:
#     print("not angestrom number")


# x = int(input("x: "))
# list = []
# for i in range(2,int(x**0.5)+1):
#     if x % i == 0:
#         print("yes")


#     else:
#         print("not")

# x = int(input("x: "))
# for i in range(x):
#     for j in range(x):
#         if j < i-1 :
#             print("*",end = " ")
        
#     print()
  

y= int(input("x: "))
x = y//2+2
for row in range(x-2,x):
    for colmn in range(row,x):
        print(" ",end = " ")
    for colmn in range(row):
        print("*",end = " ")
    for colmn in range(row-1):
        print("*",end = " ")
    print()
for row in range(x):
    for colmn in range(row):
        print(" ",end = " ")
    for colmn in range(row,x-1):
        print("*",end = " ")
    for colmn in range(row,x):
        print("*",end = " ")
    print()

# x = [" "," ",]
# for i in x:
#     print(i)


# list = map(int,input("list: ").split(","))
# # list1 = sorted(list)
# # x = list1[::-1]
# # print(x)
# for i in list:
#     print(i)

# x = "jatin"
# print(x[2])
# x = 2.3334444555
# print("{0:.2f}".format(x))

# x = input("x: ")
# y = input("y: ")
# list1 = []
# for i in x:
#     list1.append(i)
# print(list1.count(y))

# class Filternums():
#     def __init__(self,list):
#         self.list = list
#     def even_numbers(self):
#         for i in self.list:
#             if i % 2 ==0:
#                 evenlist.append(i)
#         print(evenlist)
# class oddfilter(Filternums):
#     def odd_numbers(self):
#         for i in self.list:
#             if i% 2!= 0:
#                 oddlist.append(i)
#         print(oddlist)
#     def compute_result(self):
#         print(sum(oddlist)*len(oddlist))


# list = list(map(int,input("list: ").split(",")))
# evenlist = []
# oddlist = []
# result = oddfilter(list)
# result.odd_numbers()
# result.compute_result()

# x = input("x: ").split(" ")
# list1 = []
# list2 = []
# for i in x:
#     list1.append(i)
# print(list1)
# for i in range(1,len(list1) + 1):
#     list2.append(list1[-i])
# orglist = ' '.join(list2)
# print(orglist)




# n =input()
# list1 = []
# for i in n:
#     list1.append(i)
# myset = set(list1)
# mylist =list(myset)
# org = ''.join(mylist)
# print(org)
  


# import math
# n = int(input("n: "))
# x = math.factorial(n)
# list1 = []
# for i in str(x):
#     if int(i) == 0:
#         list1.append(i)

# print(len(list1))

# n = int(input("n: "))
# x = str(n)
# list1 = []
# for i in x:
#     y = math.factorial(int(i))
#     list1.append(y)
# if n == sum(list1):
#     print("strong num")
# else:
#     print("nota a strong num")



# x = map(int,input("x: ").split(","))
# mylist = []
# for i in x:
#     if  i % 5 ==0 :
#         mylist.append("@")
#     elif i % 3 ==0:
#         mylist.append("#")
#     elif i% 3 !=0:
#         mylist.append("^")
# print(mylist)

# x = list(map(int,input("x: ").split(",")))
# list1 =[] 
# list2 = []
# mylist = []
# for i in x:
#     is_prime = True
#     for j in range(2,i):
#         if i % j == 0:
#             is_prime = False

#     if is_prime == True:
#         list2.append(i)
# for i in x:
#     if i % 2 != 0:
#         if i in list2:
#             mylist.append("#")
#         elif i not in list2:
#             mylist.append("*")
#         else:
#             mylist.append(i)
#     else:
#         mylist.append(i)
# print(mylist)



# n = map(int,input("n: ").split(","))
# list1 = list(n)
# list2 = []
# for i in list1:
#     for j in range(2,i):
#         if i % j == 0:
#             list2.append(i)
# print(list2)

# mylist = list(zip(list1,list2))
# print(mylist)
    

# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# matrix = []
# for i in range(rows):
#     row = list(map(int,input().split(" ")[:cols]))
#     matrix.append(sorted(row))


# for i in matrix:
#     for j in range(cols):
#         if j==rows-1:
#             print(i[j],end="\n")
#         else:
            # print(i[j],end=" ")









                 








  
