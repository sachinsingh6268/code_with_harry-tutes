# file name should not be time because it is a module name and it may clash with the file name
# How to calculate execution time of any program(how much time a program will to run)

# let's understand with an example
# for i in range(45):
#     print("Sachin Singh")
#
# k=0
# while k<45:
#     print("Sachin Singh")
#     k+=1

# NOW IF WE WANT TO FIND WHICH PROGRAM BETWEEN TWO OF THE ABOVE WILL RUN FAST
# for this we will use time module
# time module has a time() function which gives the time in seconds taken by program to run at that particular instant
import time
# initial=time.time()
# print(initial)
#
# for i in range(42):
#     print("SACHIN SINGH")
#
# print(f"time for for loop {time.time()-initial} seconds")
# forloop=time.time()
# k=0
# while k<42:
#     print("SACHIN SINGH")
#     k+=1
#
# print(f"time for while loop {time.time()-forloop} seconds")

# So, theoretically time taken by for and while loop is same provided we have not created any variable unnecessarily

# time module is a large module so we can read it's documentary over internet


# TO GET THE CURRENT DATE TIME AND YEAR,WE HAVE A FUNCTION IN TIME MODULE AS
# as we know time.time() returns no. of ticks with reference to a time already taken by the systet
# time.localtime() return the tick time to current time(time at the instant)
# because time returned by time.localtime() is in the form of tuple, so to convert it into the correct format we will use time.asctime()
# Let's understand with an example
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

# time.sleep() ---->it's a function in the time modules which make the program to wait for the limited amount of time