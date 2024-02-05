#fibonacci is like this 0 1 1 2 3 5 8 13  21 ...

#function to find nth term in a fibonacci series using recursive and a for loop

def fibonacci(n):
    if (n<2):
        return 1
    else:
        return (fibonacci(n-1))+(fibonacci(n-2))

n=int(input("Enter number of  terms"))
for i in range(n):
                print("Fibonacci (",i,") = ", fibonacci(i))
