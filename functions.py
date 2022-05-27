# BUILT IN FUNCTIONS
#a=5
#b=4
#c= sum((a,b))
#print(c)

# USER DEFINED FUNCTIONS, these are made with the help of "def" keyword

# function definition
#def function1():
 #   print("Hello you are in function1")

# function call
#print(function1())  **** as it does not have any return type, so it will return none

# function with parameters
#def function2(a,b):
 #   print("Hello you are in fuction2:",a+b) # this function does not have any return type

#function2(5,6)

# if we want function to return something, then we will write return statement in the function definition as
#def function3(a,b):
#    avg=(a+b)/2
 #   return avg
#average=function3(576,564)
#print("average of the two numbers is",average)

# DOCSTRING IN A FUNCTION-> it looks like comment but it's not as it's written inside a function
# ***first line written inside a function as a string is called docstring***

def function4(a,b):
    """This is a function which will calculate the first number to the power of second number"""
    rslt=a**b
    return rslt
print(function4.__doc__)  # it's very useful when we have a plenty of functions to deal with ***** "()" is not used here with the function name

# docstring tells us about the function , what it does , sometime it tells about the things that to be remembered before using a particular function


