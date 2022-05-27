# EXCEPTION HANDLING IS VERY IMPORTANT. SOMETIMES IF WE WANT TO EXECUTE CODE EVEN AFTER SOME ERROR IN CODE IN BETWEEN ,THEN WE USE IT TO CATCH THE ERROR AND TO RUN THE REMAINING
# CODE SUCCESSFULLY

# Let's understand it with an example
num1=input("Enter first number\n")
num2=input("Enter second number\n")
try:
    print("The sum of two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is very important to run anyhow")

"""these type things are mostly used when we work with internet connectivity, like when during downloading any file, if there is internet issue, it's simply shows that here is 
issue. It does not stop because it have some error in the code. That's why for such cases, exception handling is used:::::  """


# USE OF "as" KEYWORD, why we use as keyword here in exception handling