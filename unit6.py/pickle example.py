# import pickle
# a = [1,2,3,4,5,"bala"]
# with open()
# x = [2,3,4]
# a,b,c = x
# print(a + b + c)



# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
# except ZeroDivisionError:
#     print("zero devision error ocured")
# except NameError:
#     print("zero error occured")
# else:
#     sum = a*b

# finally:
#     print("ram ram ")


# class vehicle():
#     def __init__(self,name ,age) :
#         self.name =name
#         self.age = age
#     def getdetails(self):
#         print(self.name,self.age)
# class car(vehicle):
#     def __init__(self, name, age,address):
#         super().__init__(name, age)
#         self.address = address
#     def getdetails(self):
#         print(self.address,)


# class SimpleObject(): 
 
#     def setdetails (self, name): 
#         self.name = name 
#         l = list(name) 
#         l.reverse() 
#         self.name_backwards = ''.join(l)
#     def getdetails (self):
#         print(str(self.name_backwards))
# s1 = SimpleObject()
# data= []
# name = input("name : ").split(",")
# name = list(name)
# for i in name :
#     s1.setdetails(i)
# list(s1.getdetails())
# for i in name :
#     data.append(i)
# print(data)







with open('file1txt','r') as fl1:
    for i in fl1:
        print(i)

    

