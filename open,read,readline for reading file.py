# Basic syntax for reading a file
#open("sachin.txt")


# To apply different operations on a file, we make a file pointer that points to a particular file, it's different from cpp pointer but it's file handle
# open() return a file pointer of a given file as it's arguement
# f=open("sachin.txt") # now we can use this pointer for different operations
# content= f.read()
# print(content)

# IT'S ALWAYS A GOOD PRACTICE TO CLOSE A FILE AFTER IT'S USE,
#f.close() ** using close() we make a file free from all it's resources so that it can be used by others easily



# In which mode we want to open a file
# file=open("sachin.txt","rt") # ** "r" for reading and "t" for text mode, these both are default modes
# cont=file.read()
# print(cont)
# file.close()

# using arguements in the read() function


# if we use number greater than the no of characters in the file as a arguement in the read() function
# then it will read all the character that are present in the file,as


# To read the file line by line
# f=open("sachin.txt","rt")
# content=f.read()
# for line in content: # it will print the content line by line and here every character acts as a new line
#     print(line)
# for line in f: # it will print the content line by line and here every line in the file will act as a line
#     print(line,end="")  # it will not give anything because f.read() in content has already read the file once, so we have to comment out the f.read() command
    # by default it will give a new line

# readline() FUNCTION
# f=open("sachin.txt","rt")
# print(f.readline())  # it will give a new line by default
# print(f.readline())  # ----//------
# print(f.readline())  # -----//-----  # no new line character in the last line
# f.close()

# readline() function --> it's used to print lines as a list
f=open("sachin.txt","rt")
list=f.readlines()
print(list) # here we can see that these lines are containing a new line character already
