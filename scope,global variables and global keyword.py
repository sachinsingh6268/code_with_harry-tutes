# it's most common confusing concept in the python programming

l=10 # it's global variable and it can be used by any of the function in the program
# def function1(n):
#     l=5 # this l has scope only inside this function only,this can't be accessed outside the function
#     m=9 # these are called local variables as these can be accessed only inside this function, if these are not defined inside the function, then global defined will be used
#     print(l,m)
#     print(n,"I am Sachin Singh")

# function1("Hello Everyone")
# print(l) # here global varible will be printed as it's in the global scope


# GLOBAL CAN BE CONSIDERED AS GOVERNMENT PROPERTY AS IT CAN BE USED BY EVERYONE WHILE LOCAL AS THE PRIVATE PROPERTY AND CAN BE USED BY WHO OWNS THAT PROPERTY
# variables are searched from local to global level, if variable is not found locally then it will be searched globally, if it will not be found anywhere then it will throw error
# print(m) # it will give the error as m is not in the global or public scope

# WHAT WILL HAPPEN IF WE WANT TO CHANGE THE VALUE OF LOCAL VARIABLE INSIDE A FUNCTION, AS GLOBAL IS GOVERNMENT PROPERTY, IT CAN'T BE CHANGED BY ANY RANDOM, WE CAN CHANGE IT IN GLOBAL SCOPE


# IF we want to change the global variable in a function(in some local environment) then we should use "global" keyword for that
# can be done this way
# def function2():
#     global l  # this line will give the permission to change the global variable
#     l=l+45
#     print(l)
#
# function2()


# A COMMON MISCONCEPTION
def sachin():
    a=30
    def anuj():
        global a
        a=233
    print("Before calling anuj",a)
    anuj()
    print("After calling anuj",a)
sachin()  # it will give both value same because function will first search for local and then go for global variable,,here 'a' inside anuj is global so it will go outside the function & will go in global scope
print(a)  # it will print the value of 'a' that is in the global scope, so a value will be 233