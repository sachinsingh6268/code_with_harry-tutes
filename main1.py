# if we have made a file and importing it into other file then the public functionalities will run automatically in that function if we are importing that file
# let's understand with an example
# def printsachin(str):
#     return f"My name is {str}"
#
# def add_two_numbers(a,b):
#     return a+b+5
#
# print(printsachin("Sachin"))
# print(add_two_numbers(5,88))


# SO TO PREVENT THIS TO HAPPEN THAT ONLY THOSE FUNCTIONS SHOULD RUN THAT ARE CALLED EXPLICITLY, We will write the functions in public scope the following way as given below
def printsachin(str):
   return f"My name is {str}"

def add_two_numbers(a,b):
    return a+b+5

if __name__ == '__main__':
    print(printsachin("Sachin"))
    print(add_two_numbers(5,88))

# after doing this the functions will run that we have called explicitly only when this file is imported in the other function
# if we run this file this will run the same way as it runs previously