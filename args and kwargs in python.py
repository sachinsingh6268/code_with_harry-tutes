# why args and kwargs are used, what are their benefits, what were the prblms in normal arguements


# let's try to understand with an example
# def print_names(a,b,c,d):
#     print(a,b,c,d)
# print_names("Sachin","Anuj","Sahil","Arpit")
# if we forgot to add one name, then for this we have to give the name as arguement and also we have to modify the function for the same(add seperate arguement for remaining)
"""But will this way be plausible to use if we are working on a scallable program where we are dealing with millions of users simultaneously, obviously it will be impossible
to maintain millions of variables, single variable name for every single user"""




# SO TO RESOLVE THIS ISSUE WE WILL STUDY "args and kwargs" CONCEPT

# here we send the arguement as list which may contain millions of entries at a time
# * is used to convert given list to tuple,so list is converted into a tuple as we pass list with a "*"
# def funargs(*args):  # * should be used here and also in calling the function
#     for item in args:
#         print(item)
#
# list=["Sachin","Anuj","Sahil","Arpit"] # we can also make it tuple with parenthesis, then also it will be converted to tuple only so we can say to make it tuple is a convention
# funargs(*list) # * should also be used here
# THE ADVANTAGES FOR USING THIS IS THAT WE CAN ADD MORE ARGUEMENTS IN THE LIST WITHOUT WORRYING ABOUT THE FUNCTION DEFINITION
# normal arguements can also be passed with *args as
# def hybrid(normal,*args ):  # name need not to be args only it can be anything as a variable name,it's used for understanding
#     print(normal)
#     for item in args:
#         print(item)
#
# x="I have started Python programming with my friends, there names are written below:"
# arg=["Anuj","Sahil","Arpit"]
# hybrid(x,*arg)  # if we use the name of args before the normal variable,then it will give error, WHY???


# RULE OF THUMB IS THAT WE SHOULD USE FIRST WRITE NORMAL arguement, THEN *args ,THEN **kwargs, below are all valid syntaxes
# function(normal,*args,**kwargs) or function(normal,*args) or function(normal) --->this says that we can only ignore only from the right to left order not in left to right




# WHAT IS **kwargs??
# it's used to pass a dictionary as a arguement in the function as illustrated below
def function(normal,*list,**dictionary):
    print(normal)
    print("My brothers and their residences are given below")
    for item in list:
        print(item)
    for key,value in dictionary.items():
        print(f"{key} is in {value}")

normal="Hello Everyone, I am Sachin Singh"
list=["Anuj Singh","Sahil Singh","Arpit Singh"]
dict={"Anuj":"Gwalior","Sahil":"Satna","Arpit":"Nardaha"}
function(normal,*list,**dict)

# POINT TO NOTE:--- *args can't be without normal and **kwargs can't be without *args but normal can be single or with *args only or can be with both *args and **kwargs