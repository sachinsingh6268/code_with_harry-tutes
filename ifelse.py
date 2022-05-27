"""var1=45
var2=234
var3=int(input())
if var3>var1: # we can also use parenthesis here, but not using parenthesis is recommended
    print("Greater") # these 4 spaces that are created automatically are called as indentation if we remove this gap,it will give error
elif var3==var1:
    print("Equal")
else:
    print("Lesser")   # this gap that is created by default is called indentation """

    # else if in python is written as elif
#list=[23,35,54,5,25,2]
#print(23 in list)
#if 23 in list:
 #   print("Yes,it's in the list")

    # likewise "not in" is used if we want to check if it's not in the list *** note that not and in are different keywords
#list1=[23,34,53,56,12]
#print(2332 not in list1)
#if 234 not in list1:
#    print("Not in the list")

#  QUIZ
print("What is your age?")
age=int(input())
if age<7 or age>100:
    print("this is not a logical age")
elif age>18:
    print("You are allowed to drive")
elif age==18:
    print("It's difficult to tell whether you can drive or not, please visit us then we will decide")
else:
    print("You are not allowed to drive untill you are not 18+")
