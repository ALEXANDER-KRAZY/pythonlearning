#function to find gcd of numbers recursively

def gcd(x,y):
    rem=x%y
    if (rem==0):
        return y
    else:
        return gcd(y,rem)

x=int(input("Enter value of x :"))
y=int(input("Enter value of y :"))
print("GCD of these numbers is ", gcd(x,y))
