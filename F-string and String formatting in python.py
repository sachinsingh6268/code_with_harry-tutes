# f string??  ---> string formatting


# one of the simple way for string formatting
# me="Sachin"
# al="Singh"
# a="My name is %s %s"%(me ,al)
"""as here is only one variable is used,so we are not having any issue,but if we have many variable then we should remember the numbering to insert the variables
,then we will have problems on inserting strings in between """
# print(a)


# another method where also may be poor readibility when inserting large data
# me="Sachin"
# al="Singh"
""" if indexing is not given in the curly brackets then it will take the format as given inside the "format" function given below , but if we want to change the order
we can specify the order in the curly brackets"""
#a="My name is {} {}"
# a="My name is {1} {0}" # here in this case al will be at first place and me at the last
# b=a.format(me,al)
# print(b)


# SO TO RESOLVE ALL THE ISSUES THAT ARE CAUSED ABOVE, PYTHON INTRODUCES CONCEPT OF "f string" and f string IS FAST AS COMPARED TO OTHER METHODS AND f STANDS FOR FAST HERE IN f string
# if we use "f" before writing the string in a variable, then it's called "f string"
# a = f""  #----> this is an example of f string
# in f string we can write the varible name inside the curly brackets so all the problems will be gone,we can write as
import math
me="Sachin"
al="Singh"
# if we want to use expression ,then it can also be used in "f string"
a=f"My name is {me} {al} {5*234} {math.cos(577)}"
print(a)


# Explore "time" module