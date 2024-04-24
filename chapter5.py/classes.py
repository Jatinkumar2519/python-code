# class car:
#     def __init__(self,c1 , n1):
#         self.color = c1
#         self.name = n1
#     def getspeed (self,speed):
#         print("the speed of car:",self.name,"and speed:",speed,"km/hr")

# # object1
# # speed = int(input("speed: "))
# car1 = car("red","Honda")
# car1.getspeed(int(input("speed: "))) 

# # accessing property
# print("color:",car1.color)
# print("name:",car1.name)

# # object2
# car2 = car("white", "supra")
# car2.getspeed(int(input("speed: ")))

# # accessing property
# print("car name:",car2.name)
# print("car color:",car2.color)


class STUDENT():
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    def printAverage(self,marks):
        print("average:",(sum(marks))/len(marks))
    def properties(self):
        print("name:",self.name ,"age:",self.age , "school:",self.school)


# student1
student1 = STUDENT('Raj', '20', 'CSE')
student1.printAverage(int,input("marks:").split(","))
# name = input("name: ")1 2 3 45 6 6

