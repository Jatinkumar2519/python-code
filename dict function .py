# data1  = input("Enter Keys:").split(",")
# data2 = input("ENTER VALUESS:").split(",")
# mydict= dict(zip(data1,data2))
# #  using  methods#
# print("dictonary keys are:",mydict.keys())
# print("dictonary values are:",mydict.values())
# print("sorted dictonary:",sorted(mydict.items()))
# print("using get:",mydict.get("red"))
# seq = (12, 13, 14)
# dict2 = {}
# print("using from keys:",dict2.fromkeys(seq, 20))
# #  using setdefault
# print("using setdefault:",mydict.setdefault("red",10))

n = 5
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(" ",end = " ")
    print()
    c = 1
    for j in range(1,i+1):
        print(" ",c,sep=" ",end=" ")
        c = c*(i-j)//j
    print()