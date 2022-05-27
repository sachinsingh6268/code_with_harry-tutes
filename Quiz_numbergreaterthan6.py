list=["sachin",23,35,"yes",4,38,"as35e,",3,1,3,4,45,"my name is anuj",23,32,23,"no"]

#for item in list:
 #   if type(item) is int and item>6:
  #      print(item)
             # OR
#for item in list:
 #   if item.isnumeric() and item>6:  # it will give error because int data type does not have any isnumeric function
  #      print(item)
  # SO TO REMOVE THE ABOVE ERROR WE HAVE TO FIRST TYPECAST TO STRING SO THAT WE CAN USE THE FUCTION "isnumeric"

for item in list:
    if str(item).isnumeric() and item>6:
        print(item)

