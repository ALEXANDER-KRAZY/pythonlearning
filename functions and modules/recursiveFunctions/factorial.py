#function to calculate factorial of a number recursively

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter value of n "))
print("Factorial of n is :", factorial(n))
