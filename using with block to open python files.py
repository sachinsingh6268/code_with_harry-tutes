# WITH BLOCK TO OPEN PYTHON FILE


# normal way to open a file is
# f=open("sachin.txt","rt") # rt--> it's taken by default
# print(f.readlines()) # after it's execution file pointer will point to the end of the file and then nothing will left if we try to read using read() or readlines() or readline()
# print(f.readline())
# f.close()

# opening a file with the help of,so here we need not to close the file explicitly
with open("sachin.txt") as f:  # it take care of both opening and closing of a file
    print(f.readlines())

