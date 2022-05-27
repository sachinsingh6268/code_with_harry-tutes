#----------------------- MAP FUNCTION IN PYTHON

# numbers=["3","323", "23"]
# if we want to convert the elements of the list into integers from string
# numbers[2]=int(numbers[2])+1
# print(numbers[2])

# and to convert all the elements to integer we have to run the loop as

# this is not the correct way , think why?
# for item in numbers:
#      item=int(item)
# numbers[2]=numbers[2]+2
# print(numbers[2])


# this is the correct way to typecast
# for i in range(len(numbers)): # anything inside range should be a number
#     numbers[i]=int(numbers[i])
#     print(numbers[i])

# USING MAP IT(typecasting) CAN BE DONE IN A SINGLE LINE (because using loop again & again is not good thing) AS
# map(int,numbers)
"""first aguement tells about which function we want to apply on each of the element in the list and second arguement tells about the list on whose elements the function
is applied. map function returns the object"""

# print(map(int,numbers))

# so we have to convert it into list as
# numbers=list(map(int,numbers)) # -->typecasting into list from the object returned by map function
# numbers[1]+=23
# print(numbers[1])


# let's do square of all the elements given in the list
# lst=[2,232,23,5,7,3,4]
# first make a function that convert a number into square as
# def sq(a):
#     return a*a
# # now using map function we will convert every element of list into square of it as
# square=list(map(sq,lst))
# print(square)

# USING LAMBDA FUNCTION(lambda is a one liner function) as
# square=list(map(lambda x:x*x,lst))
# print(square) # now it will give the same rslt in a single line of code

# ANOTHER INTERESTING USE OF map
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))  # x is the element of func list here
#     print(val)  # look at the answer and observe for the same



#------------------------- FILTER FUNCTION IN PYTHON

# filter function does filtering---> it makes such a list of elements on which a given function returns true let's understand with the help of an example
# list1=[1,2,3,4,5,6,7,8,9,10,11,13]
# def is_greater_6(num):
#     return num>6
# gr_than_6=list(filter(is_greater_6,list1))  # this is the basic,explore advanced functionalities yourself
# print(gr_than_6) # it will give all the elements greater than 6 in the list


# ----------------------------- REDUCE FUNCTION IN PYTHON
# reduce is part of "functools" module
# let's understand reduce with an example,if we want some of all integers in list then there can be more than one way as
# first method is
list1=[1,2,3,4,5,6,7,8,9]
# num=0
# for item in list1:
#     num+=item
# print(num)  # as we know it will work fine but we need to write this small task, so we will try to make our code more pythonic

# same above code in one line can be written as follows
from functools import reduce
sum=reduce(lambda x,y:x+y,list1)
print(sum) # answer will be same as of the above

# to multiply we can use '*' insteas of '+' as
pro=reduce(lambda x,y:x*y,list1)
print(pro)



# sometimes such functions give good performance over normal functions and in some cases we have to write less codes as compared to normal codes
