# FAULTY CALCULATOR
operator=input("Enter the operator you want to execute on: ")
n1= int(input("Enter the first number of your choice: "))
n2= int(input("Enter the second number of your choice: "))
if n1==56 and n2==9 and operator=="+":
    print(77)
elif n1==45 and n2==3 and operator=="*":
    print(555)
elif n1==56 and n2==6 and operator=="/":
    print(4)
elif operator=="+":
    print(n1*n2)
elif operator=="-":
    print(n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print("Please choose the operator that is present here!")