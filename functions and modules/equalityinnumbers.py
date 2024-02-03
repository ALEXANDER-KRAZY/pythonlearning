#function to check equality of two numners

#function defination
def equality(a, b):

#conditional defination
    if (a==b):
        return 0
    if (a>b):
        return 1
    if (a<b):
        return -1

#prompt user to enter numbers
a = int(input("Enter number: "))
b = int(input("Enter number: "))
res = equality(a, b)

#condition execution
if (res==0):
    print("a is equal to b")
if (res==1):
    print("a is greater than b")
if (res==-1):
    print("b is greater than a")