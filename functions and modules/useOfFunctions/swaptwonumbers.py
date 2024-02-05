#function to swap two numbers

def swap(a,b):
    a,b = b,a
    print("After swap :")
    print("First number =", a)
    print("Second number =", b)
    
a = int(input("Enter first number"))
b = int(input("Enter second number"))
 
print("Before swap :")
print("First number =", a)
print("Second number =", b)

   
swap(a,b)
