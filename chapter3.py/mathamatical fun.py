num = int (input(" "))
def f1(num):
    return num*2
def f2(num):
    return num**2
print(f2(f1(num)))