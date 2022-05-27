#list=["sachin","anuj","arpit","sahil"]
#for x in list:
 #   print(x)
# same way it can also be used for tuple,list of list,tuple of tuple, list of tuple,etc...

#tuple=("sachin","anuj","sahil","arpit")
#for items in tuple:
 #   print(items)

 # list of list
list1=[["sachin",23],["anuj",20],["sahil",17],["arpit",14]]
#for item,age in list1:
 #   print(item,"and age is",age)

# typecast a list of list into a dictionary using a keyword  **dict**
dict1=dict(list1)

# only to obtain keys from the dictionary
#for item in dict1:
 #   print(item)

#print(dict1)
#for item,lollypop in dict1:
 #   print(item,lollypop) # IT WILL GIVE AN ERROR
 
# FOR THIS ERROR TO IGNORE WE WILL USE dict1.items() instead of dict1 in for loop
for item,age in dict1.items():
    print(item,"and age is",age)