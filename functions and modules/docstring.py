#teh string can be called using the __doc__ word of the function
#in case of multiple lines of a doc string the second line should be blank
def greets():
    """We shall print a greeting on the screen.
    Print just hello"""
    print("hello")
print(greets.__doc__)