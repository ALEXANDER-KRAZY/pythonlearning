#function to see if number is even or odd

def evenodd(a):
    if (a%2==0):
        return 1
    else:
        return -1
       
a = int(input("Enter number : "))

if (evenodd(a)==1):
    print("Number is even")
else:
    print("Number is odd")