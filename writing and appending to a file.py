# f=open("sachin.txt","w") # "w" is written here bcz we want to write on the file, and as nothing is written so it will be by default text file
# f.write("Sachin has completed his 3rd year recently in May of 2022") # write() function will empty the file each time and update it with the content that we will provide in the write as arguement
# f.close()

# but in most of the cases we need to append(adding at the last of the file) something to the file without first emptying the file and then adding something
# f=open("sachin.txt","a")
# number_of_character_appended=f.write("It's my own way\n")  # the number of times we will run the program, each time it will append the line each time
# print(number_of_character_appended) # will tell about how many characters we have appended in the file
# f.close()
# SO f.write() FUNCTION RETURNS THE NUMBER OF CHARACTERS THAT ARE WRITTEN IN THE FILE


# handle read and write both
f=open("sachin.txt","r+")  # here by opening file once only, we can use both read and write operations simultaneously
print(f.read())
f.write("thank you")
f.close()