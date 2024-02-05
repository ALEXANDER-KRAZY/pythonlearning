#function to find exponent(raised to power) of a number using recursive

def exp(x,y):
    if (y==0):
        return 1
    else:
        return x*exp(x,y-1)

x=int(input("Enter value of x :"))
y=int(input("Enter value of y :"))
print("Result is ", exp(x,y))
