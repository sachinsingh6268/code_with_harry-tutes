# import main1 as m1 # on importing the file all the functions that are in public domain will run automatically
# print(m1.printsachin("Sachin"))
# print(m1.add_two_numbers(5,43))



"""now if we import the file "main" here then by default the functions written in public domain will get executed,so to prevent this use main as
we use in c and cpp when start writting functions"""

import main1
print(main1.printsachin("Sachin"))
print(main1.add_two_numbers(23,3534))