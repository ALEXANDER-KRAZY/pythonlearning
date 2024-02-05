#lambda functions are not defined using the **def** keyword
#instead are created using the **lambda** keyword

#write a code to add two numbers

sum = lambda x, y : x + y
print("sum = ", sum(5,2))
#above code is same as the following code.
def sum(x, y):
    sum = x + y
    print("sum is ", sum)
sum(9, 10)
    