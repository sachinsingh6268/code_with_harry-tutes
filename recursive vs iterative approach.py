# recursion ---> using a function inside a function is called recursion

# ITERATIVE APPROACH
# def fact(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
#
# print(fact(int(input("Enter the number\n"))))

# RECURSIVE APPROACH
# def fact(n):
#     if(n==1):
#         return 1
#     return n*fact(n-1)
#
# print(fact(int(input("Enter the number\n"))))

# FIBONACCI SERIES

def fib_nac(n):
    if(n==1):
        return 0
    elif n==2:
        return 1
    else:
        return fib_nac(n-1)+fib_nac(n-2)


print(fib_nac(int(input("Enter the number\n"))))