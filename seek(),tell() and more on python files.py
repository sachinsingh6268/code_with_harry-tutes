# these seek() and tell()  are very important to use

# f=open("sachin.txt") # file pointer or file handle
# print(f.tell()) # it tells us about where our file pointer is in the file currently, IT'S VERY USEFUL WHEN WE ARE DEALING WITH THE LARGE FILES
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()


# if we want file pointer position as per our need then we will use seek()
f=open("sachin.txt","rt")
print(f.readline())
f.seek(0) # it will again put the file pointer at the 0th position
print(f.readline())  # as pointer at 0th position, it will again print the same line of file
f.close()
## ** MAKE SURE YOU ALWAYS CLOSE THE FILE AFTER USE,it's a good practice


