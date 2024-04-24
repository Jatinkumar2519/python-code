# def printuser(name ,age):
#     print("name = ",name)
#     print("age = ",age)
# printuser(13, "john")
# printuser(name = "jphn", age = 14)



# def printuser1(*, name ,age):   
#     print('name =', name )
#     print('age = ', age )
# printuser1(name = "john",age = 14)
# printuser1(age = 20 ,name = 'peter')




# def simplecalc(a = 120,b=180):
#     print('addition:',a+b) 
#     print('subtrection:',a-b)
#     print('multiplication:',a*b)
# a = int(input("num1: "))
# b = int(input('num2: '))        
# simplecalc()



def sayhello(users):
	greet = "Hello " + users
	# print(greet)
	
users = ['Ram', 'Mahesh', 'Vasudha', 'Uma', 'Sekhar', 'John']

for i in users:
    print("heloo",i)
sayhello(i)