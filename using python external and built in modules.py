# if we are using any of the module then it must be self understood that the code that we are using with the help of module is written in the backend
# code of any module can be accessed by using "crtl" key and by clicking on that module name, this way we will get the code that is written in the backend for the module

import random #---> it is the name of the module
# modules may contain submodules and function that we can use directly by accessing the modules directly
# we need not to learn function of the module, we can read the documentary for the module and can use them in our program directly
# if we are not using any module then it will be in grey color and if we will use it in our program then it's color will change as illustrated below
# random_number=random.randint(2,23) # any number between 2 and 23 including both the numbers
# print(random_number) # it is one of the function of random module

""" "random.random"  ----> while random.randint(a,b) generates only interger between the given number while random.random() will generate any number that is in between 0 and 1
these two numbers """
# random_num=random.random()  # it generates number between o to 1
# print(random_num)

# to get larger number we will multiply the appropriate number as random_num=random.random()*100
# random_numb=random.random()*110 # it will create any number between 0 and 110, number here is not integer but a normal number
# print(random_numb)

# to choose a random element from a list,we will use random.choice(list_name) as given below
# list=["Sachin","Anuj","Sahil","Arpit"]
# choice=random.choice(list)
# print(choice)

"""sometime it may be the case that we don't have particular module not installed, so to install particular module GO TO PYCHAM TERMINAL AND WRITE "pip install" followed by module
name"""

# "sklearn(scikit learn) is most useful and robust library for machine learning in python
 
