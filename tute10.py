#dictionary is nothing but key value pair represented by curly bracket -> {}
#d1={}
#d2={1:"sachin",2:"Anuj",3:"Sahil",4:"Arpit"}
#print(d2)
# to access value of particular key
#print(d2[1])
# A dictionary can contain another dictionary
d3={"sachin":"Chicken","Anuj":"Egg Curry","Sahil":{"Chicken":"Tanduri","Egg":"Omelate","Paneer":"Kadahi"}}
#print(d3["Sahil"])
#print(d3["Sahil"]["Chicken"])

# insertion of key value pairs other than the time of dictionary creation
d3["Arpit"]="Only Roti and Vegetables"
#print(d3)

# insertion with different data type of key and value
d3[2342]="I don't like anything that you have"
#print(d3)

# to delete a particular key, value pair from dictionary -> del is used for this purpose
#del d3[2342]
#print(d3)

# difference between copy fuction and assignment operator while creating copy of a dictionary*******
# d4=d3 vs d4=d3.copy()
# d3.copy() will return the shallow copy to d4 which will have no dependence on d3
""" d4=d3 will create a reference of the same dictionary d3, so as it will point to d4 , any change that we will be made on any of the dictionay will 
reflect in the other dictionary too. Here no copy is created rather same is pointed by two pointing dictionaries now"""

#print(d3.get("Arpit"))
# to update the dictionary or to add new member in the dictionary
d3.update({"RishiKesh":"Milk"})
#print(d3)
#print(d3.keys())
#print(d3.items())
#print(d3.values())