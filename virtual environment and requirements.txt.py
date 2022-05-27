# WHY THIS TOPIC IS IMPORTANT???
"""Ans-- when we work on a big project like game development ,website development ,data analysis etc. with the help of python, then we need that our program should run
continuously always (why we are saying that program should run continuously because the packages in the python are updated time to time that means old functions will
get outdated(deprecate) and new functions will be inserted and sometime we want to freeze our functins so that our program runs as it is always without any modifications in it)
to handle some of these cases we use virtual environment"""



# what are virtual environment, what are their work, how they are beneficial, what else we can do with the help of virtual environment
# to use virtual environment we have to do "pip install virtual environment"
# WHAT IS VIRTUAL ENVIRONMENT???
"""Ans-- if I have made a project(a website for nitj library) with help of python flask in which I have used one of the version of flask and used version 2.0 and 2.1 version
is released recently,now I sent the code of the website to one of my friend and when my friend installed then the version was pip 2.1 sklearn(another version than that I 
used) now due to this(different versions) there may be problems(because some of the functions in previous version may be deprecate and some new functions would have been 
introduced in the newer version. But we don't want such problems to face, for that we will create a virtual environment (because virtual environment takes care of all the
other versions and make sure that the code written runs as expected and ignores(take care of newer version) the new functionalities due to version change)
SUMMARY---> so virtual machine ensures that program uses only the functions of the version in which code is written,so this way we will get rid off the prblm mentioned above
"""

# we will write "pip install virtualenv" to install "virtualenv" packages
"""creating new virtual environment means using base interpretor forming a new form of python interpreter,means a new python is borning that is inside the folder that we 
have created now we have no link with our own python,it's cloning that python in a new folder it's inserting a new python inside the function that we have
 created(sachin is the name here)"""
"""now in the new environment created if we try to import pandas then there will be no such module because it's totally differnt from the basic python interpreter, we have 
installed pandas but in outer interpreter, we are currently in the virtual environment so it will use python environment that is inside "sachin" folder"""
# we can also unistall modules and packages from the virtual environment writting "pip uninstall package_name"

"""USING VIRTUAL ENVIRONMENT WE CAN HAVE A CODE MEANINGFUL EVEN AFTER A LONG SPAN OF TIME,so to store all the documentary about the packages used long time ago(it also may be 20,30
years of time),so we attach a "requirement.txt" file to the user who is using the code after a long time in which names of all the packages will be there that I have installed
while writting the long time ago(as "requirement.txt" will be same after a long time) so with the help of this file user can replicate the code according to today's defined 
functions in the recently released versions. requirement.txt is not written manually,instead we will run a command in pip called "pip freeze > requirement.txt" then it will create a 
file automatically in the folder where virtual environment is created ,,in this case folder name is 'sachin'"""

# what to do if "requirement.txt" file having large number of packges and their versions,then how to install them in order to replicate the code
# for this in windows shell write the command "pip install -r directory_of_(requirement.txt)_file",then it will install all the packages contained in the file one by one


""" if we want to make a virtual environment which should contain all the packages(site packages) that are contained by our system python or base interpreter for this we write a command as
"--system-site-packages virtual_environment_name" after creation of this virtaul environment all the packages in base interpreter will be in the new virtual environment"""
