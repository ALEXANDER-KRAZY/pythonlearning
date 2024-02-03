#function to return full name of a person

def name(firstname, lastname):
    separator = ' '
    fullname= firstname + separator + lastname
    return fullname
firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
separator = ' '
fullname= firstname + separator + lastname

print(fullname)