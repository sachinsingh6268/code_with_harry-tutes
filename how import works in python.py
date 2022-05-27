# import sklearn as sk
# print(sk.__version__)
# when we import a module then it's assigned to current scope here current scope is global



# Now we want to know from where this module comes from for this we will do the following
# import sys
# print(sys.path)  #-->this is the set of paths where interpreter searchs for the modules



"""we can make a file and can import data or variables from that file in the other files
because now these files will act as a user-defined modules that user has created for his/her convinience """
# import file
# print(file.a)  #--->example of user-defined module  THIS IS RECOMMENDED PRACTICE



# if we want to access a from file directly then we can write this way
# from file import a
# print(a)
"""--->here we can use a directly --- THIS IS NOT RECOMMENDED PRACTICE TO USE because two files that we have imported may have same variable name and interpreter will get
confused which variable is from which of the file. As first way explicitly gives the file name so it's more preferred to avoid any such confusion"""


import file as f
f.printsomething("Hello I am so FUNNY")

"""SO we can say that if we are using any function many number of time in a program then we can make a file of such functions and when required we can import them and can
use them when required, it will save a lot of time ,it will be very beneficial when we work on a large project although this is naive approach to make a package, we will study
further how to make a package that is scable and more user/programmar friendly"""

"""NEVER MAKE A FILE NAME AS THE NAME OF EXISTING FILE NAME, it may cause problem to us because interpreter always first search in the current directory for searching the module 
functions and variables"""
