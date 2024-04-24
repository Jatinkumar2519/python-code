# import random
# points = 0
# number = int(input("chosse a number: "))
# if  1 <= number <= 6 :
#     randnum = random.randint(1,6)
#     if randnum == number :
#         points += 10 
#         print("you win {} points".format(points))
#     else:
#         print("number not match.you lose this game try again")
# else:
#     print("pls enter number between 1 to 6")




# cpu = [ "rock","paper","scissors"]
# your_scor = 0
# cpu_scor = 0
# played = 0
# cases ={
#     "rock": {"rock": "draw", "paper": "lose", "scissors": "win"},
#     "paper": {"rock": "win", "paper": "draw", "scissors": "lose"},
#     "scissors": {"rock": "lose", "paper": "win", "scissors": "draw"},
# }

# x = random.randint(0,2)
# y = cpu[x]
# for i in range(0,3):
#     you = input("rock,paper or scissors : ").lower()
#     if you not in cpu:
#         print("enter valid choisse")
#     else:
    
#      result = cases[you][y]
#      if result == "lose":
#         cpu_scor = cpu_scor + 1
#         played = played + 1
#         print("try! again")
#      elif result == "draw":
#         your_scor = your_scor + 1
#         cpu_scor = cpu_scor + 1
#         played = played + 1
#         print(" 1 point each")
#      else: 
#         your_scor = your_scor + 1
#         played = played + 1
#         print("you got 1 point")
# print("your's scor:",your_scor)
# print("cpu's score:",cpu_scor)





# x = input("please enter your e-mail id sir: ")

# mylist =x
# surnamelist = []
# reversedomain = []
# for i in mylist:
#     if i.isalpha() or i.isnumric():
#         surnamelist.append(i)
#     else:
#         break
# reverse= mylist[::-1]
# for i in reverse:
#     if i.isalpha() or i == ".":
#         reversedomain.append(i)
#     else:
#         break
# domain = reversedomain[::-1]
# domain1 = ''.join(domain)
# surnamelist1 = ''.join(surnamelist)
# print("domain:",domain1)
# print("surname:",surnamelist1)


# # import string
# leters = "abcdefghijklmnopqrstuvwxyz"
# leters1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# list = []
# list1 = []
# for i in leters1:
#     list1.append(i)
# for i in leters:
#     list.append(i)
# x = int(input("enter the length of pwd: "))
# y = ["@","#","?"]

# pwd = []
# for i in range(x//2):
#     pwd.append(str(random.randint(1,x)))
# for i in range(x//):
#     pwd.append(list[(random.randint(1,len(list)))])
#     pwd.append(list1[(random.randint(1,len(list1)))])
# for i in range(2):
#     pwd.append(y[random.randint(0,2)])
# passkey = ''.join(pwd)
# print(passkey)




        


# x = int(input("x: "))
# listkeys = []
# listvalues = []
# for i in range(x):
#     keys = input("keys: ")
#     listkeys.append(keys)
# for i in range(x):
#     values = input("values: ")
#     listvalues.append(values)
# mydict = dict(zip(listkeys,listvalues))
# print(mydict)





# class area():
#     def __init__(self,l,b,h):
#         self.l = l 
#         self.b = b
#         self.h = h
# class cube(area):
#     def getvalue1(self):
#         print(6*self.l*self.l)
# class cuboidal(cube):
#     def getvalue2(self):
#         print(2*(self.l*self.h + self.h*self.b + self.b*self.l))
# a=cuboidal(2,4,6)
# a.getvalue1()
# a.getvalue2()

# x = input("x: ")
# alphabet = []
# number = []
# symbol = []

# for i in x:
#     if i.isalpha :
#         alphabet.append(i)
#     if i.isnumeric:
#         number.append(i)
#     else:
#         symbol.append(i)
# alphabet = ''.join(alphabet)
# number = ''.join(number)
# symbol = ''.join(symbol)
# print("alphabet:",alphabet)
# print("number:",number)
# print("symbol:",symbol)



# x = int(input("x: "))
# y = 1
# for i in range(x+1):
#     for j in range(1,i+1):
#         print(j,end = " ")
        
        
#     print()


# x = int(input("x: "))
# for i in range(x+1):
#     for j in range(i):
#         print("*",end = " ")
#     print()
# for i in range(x):
#     for j in range(i,x-1):
#         print("*",end = " ")
#     print()




# x = int(input("x: "))
# mylist = []
# for i in range(x):
#     num = int(input("num: "))
#     mylist.append(num)
# print(mylist)
# print(max(mylist))

# x = map(int,input("x: ").split(" "))
# n = int(input("x: "))
# try:
#     for i in range(n-1):
#         print(i)
# except ValueError:
#     print("invalid index")
        

# x = int(input("x: "))
# days = ["Sunday","Monday","Tuesday","Thrusday","Friday","Saturday"]
# if x > len(days) or x < 0:
#     print("invalid value")
# else:
#     print(days[x])


# x = input("x: ")
# y = "abcdefghijklmnopqrstuvwxyzabcd     "
# alphabetlist = []
# stringlist = []
# list = []

# for i in y:
#     alphabetlist.append(i)
# for i in x:
    
#     stringlist.append(i)
# for i in stringlist:

#     s = alphabetlist.index(i)
#     j = alphabetlist[s+4]
#     list.append(j)

        
# orginallist =''.join(list)
# print(orginallist)


# x = int(input("c: "))
# list1 = []
# list2 = []
# originallist = []
# for i in range(x):
#     list1.append(i)
#     list2.append(i)
# for i in range(len(list1)):
#     sum = list1[i] + list2[i]
#     originallist.append(sum)
# print(originallist)



# x = input("x: ")
# y = " abcdefghijklmnopqrstuvwxyz "
# alphabetlist = []
# stringlist = []
# mathameticalname =[]
# for i in y:
#     alphabetlist.append(i)
# for i in x:
#     stringlist.append(i)
# for i in stringlist:
#     s = alphabetlist.index(i)
#     mathameticalname.append(str(s*s))
# math =''.join(mathameticalname)
# print(math)

 
# x = int(input("x: "))

# y =list(map(int,input("list: ").split(",")))
# # for i in range(len(y)):12,
# #     z = int(y[i])
# #     list.append(y)
# list1 = sorted(y)
# if (max(list1)) > 50:
#     print(list1)
# elif (max(list1)) < 50:
#     print(list1[::-1])
# else:
#     print(list)



# data = map(int,input("data: ").split(" "))
# data = list(data)
# mylist = []
# for i in data:
#     if data.index(i) % 2 != 0:
#         mylist.append(int(i))
# print(mylist)

        

# y = input("x: ")
# if len(y) > 2:
#     if len(y) % 2 == 0:
#         print(y[0]+y[len(y)//2 - 1:len(y)//2 + 1]+y[-1])
#     else :
#         print(y[0]+y[len(y)//2]+y[-1])
# else:
#     print("invalid length of string")


# n = input("n: ")
# for i in range(0,len(n)+1):
#     # print(n[:i])
#     for j in range(i+1):
#         print(n[j],end= "")
    # print()


# class feecalculator():
#     def setdetails(self,name,rollno,fee,attendence):
#         self.name = name 
#         self.rollno = rollno
#         self.fee = fee
#         self.attendence = attendence
#     def totalfee(self):
#         if self.attendence <= 50 :
#             print(self.fee*0.02 + self.fee)
#         if  50 < self.attendence <= 75:
#             print(self.fee*0.15 + self.fee)
# name = input("name: ")
# rollno = int(input("rollno: "))
# fee = int(input("fee: "))
# attendence = float(input("attendence: "))
# x = feecalculator()
# x.setdetails(name,rollno,fee,attendence)
# x.totalfee()


# x = int(input("x: "))
# y = list(map(float,input("y: ").split(",")))
# average = sum(y)/x
# print("{0:.2f}".format(average))
# mylist = []
# for i in y:
#     if i > average:
#         mylist.append(i)
#     # else:
#     #     pass
# print(len(mylist))



# x = input("x: ").split(" ")
# mylist= list(x)
# list1 = []
# for i in range(len(mylist)):
#     if mylist[i] == mylist[i][::-1]:
#         list1.append(int(mylist[i][::-1]))
# if len(list1) > 1:
#     print(max(list1)*min(list1))
# if len(list1) == 1:
#     print(list1[0]*list1[0])


# class people():
#     def setname(self,name):
#         self.name = name 
#     def getname(self):
#         print(self.name)
# class Student(people):
#     def setage(self,age):
#         self.age = age
#     def getage(self):
#         print(self.age)
# name = input("name: ")
# age = int(input("age: "))

# s1 = Student()
# s1.setname(name)
# s1.setage(age)
# s1.getname()
# s1.getage()

# x= map(int,input("x: ").split(" "))
# mylist = list(x)
# list1 = []
# for i in range(mylist[0],mylist[-1]):
#     is_prime = True
#     for j in range(2,i):
#         if i % j == 0:
#             is_prime = False
#     if is_prime == True:
#         list1.append(i)
# print(list1)

# x = map(int,input("x: ").split(" "))
# list1 = list(x)
# mylist = []
# list= []
# if list1[0] > 1 and list1[0] < list1[1]:
#     for i in range(list1[0],list1[1]+1):
#         is_prime = True
    
#         for j in range(2,i):
#             if i % j == 0 :
#                 is_prime = False
            
#         if is_prime == True:
#             mylist.append(i)
#     for i in range(list1[0],list1[1]+1):
#         if i  not in mylist:
#             list.append(i)
#     print(tuple(list)[::-1])
# else :
#     print('invalid number')

# x = int(input("x: "))
# list1 = []
# list2 = []
# for i in range(x):
#     y = int(input("y: "))
#     list1.append(y)
# for i in list1:
#     z = i**3
#     list2.append(z)
# mytuple = tuple(zip(list1,list2))
# print(mytuple)


# n = int(input("x: "))
# x = str(n)
# list1 = []
# for i in x:
#     list1.append(int(i))
# print(sum(list1))
# alpha = 1
# for i in range(len(list1)):
#     y = alpha*list1[i]
#     alpha = y
# print(alpha)
# print(list1.count(0))


# n = int(input("n: "))
# teamlist = []
# scorelist = []
# for i in range(n):
#     x,y = input().split(" ")
#     teamlist.append(x)
#     scorelist.append(int(y))

# sortedlist = sorted(scorelist)
# z = sortedlist[-2]
# s = scorelist.index(z)
# print(teamlist[s])

# class sentencejoiner():
#     def __init__(self,str1):
#         self.str1 = str1
# class joinsentence(sentencejoiner):
#     def __init__(self,str1,str2):
#         self.str2 = str2
#         super().__init__(str1)
#     def orginialstr(self):
#         print(self.str1+self.str2)
# str1 = input("str1: ")        
# str2 = input("str2: ")
# s1 = joinsentence(str1,str2)
# s1.orginialstr()




# class CharacterCounter():
#     def setString(self,name):
#         self.name = name 
#         for i in self.name:
#             list1.append(i)
#     def countCharacter(self,char):
#         self.char = char
#         return list1.count(char)
# name = input()
# char = input()
# list1 = []
# counter = CharacterCounter()
# counter.setString(name)
# result = counter.countCharacter(char)
# print(result)


# n = input()
# list1 = []
# list2 = []
# for i in n:
#     if i.isalpha():
#         list1.append(i.upper())
# mylist = ''.join(list1)
# print(mylist)
# print(len(n))
# print(len(list1))

# n = input("n: ").split(",")
# list2 = list(n)
# list1 = []
# i = 2
# for x in n:
#     while (int(x) != 1):
#         z = int(x)%i
#         if z == 0:
#             x = int(x)//i
#             list1.append(i)
#         else:
#             i = i + 1
# # orglist = list(zip(list1,list2))
#     print(list1)
# print(orglist)


# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# matrix = []
# for i in range(rows):
#     row = sorted(list(map(int,input().split(" ")[:cols])))
#     matrix.append(row)
# matrix.sort()
# for i in matrix:
#     for j in i:
#         if j==i[-1]:
#             print(j,end="\n")
#         else:
#             print(j,end=" ")

        


# x = input()
# list1 = []
# for i in x:
#     list1.append(i)

# if len(x) > 2:
#     print(x[0:len(x) - 1]*2+x[1:len(x)]*3+x[::-1])
# else:
#     print("invalid")

# x = int(input("any num: "))
# x = str(x)
# alphabet = " abcdefghijklmnopqrstuvwxyz"
# list1 = []
# strt = 0
# list2 = []
# list3 = []
# for i in range(len(x)//2):
#     list1.append(x[strt:strt+2])
#     strt = strt + 2
# print(list1)
# start = 0
# for i in x:
#     if int(i) >= 26:
#         for j in str(i):
#             list2.append(j)
#             j = alphabet[int(list2[start])]+alphabet[int(list2[start+1])]
#         list3.append(j)
# print(list3)




# n = int(input("n: "))
# for i in range(n-1):
#     for j in range(i+1):
#         if j==i or j ==0:
#             print("*",end = " ")
#         elif j>0 or i< j:
#             print(" ",end=" ")
        
#     print()


# x = input().split(" ")
# y = input().split(" ")
# list1 = []
# list2 = []
# list3 = []
# voval = ['a','e','i','o','u']
# list4 = []
# for i in x:
#     list1.append(i)
# for i in y:
#     list2.append(i)
# for i in list1:
#     if i in list2:
#         list3.append(i)
# if len(list3) == 0:
#     print("empty")
# else:
#     print(list3)
#     for i in list3:
#         for j in i:
#             if j in voval:
#                 list4.append(i)
# for i in range(0,len(list4)):
#     print(list4[i])


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

        




