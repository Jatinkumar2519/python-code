# # name ="jatin"
 # print("GOOD AFTERNOON",name)
 # name =input("ENTER YOUR NAME")
 # print("good morning" , name)
 # a = 45
 # b = 500
 # print("THE RIMAIMDER OF A AND B IS:",a/b)
 # a =input("34.45")
 # a =float()
 # print("a")
 # # print(type(a))
 # a =4456
 # b =4499
 # avg = (a + b)/2
 # print("THE AVG. OF A AND B IS :",avg)
 # a =99
 # square = a*a
 # print ("THE SQUARE OF A IS :",square)


num = 10
sum = 0
for i in range(num-1):
    for j in range(i+1):
        if(j==0 or j==i ):
            print("*",end= " ")
        elif(j>0 and j<i):
            print(" ",end=" ")

    print()
for i in range(num):
    print("*",end=" ")
print()
# print("* "*10)



# x = input("x: ")
# b = ""
# for i in x:
#     if i.isalpha:
#         i.upper()
#         b = b + i
#     else:
#         pass
# print(b)

    


# num = int(input("num: "))
# i = 0
# print("* ")
# for i in range(num-1):
#     print("* "+"  "*i+"* ")
# print("* "*(num+1))