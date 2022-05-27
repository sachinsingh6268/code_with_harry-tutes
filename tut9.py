todolist=["python","c++","sql","projects","dbms","data structure and algorithms","contests",52]
#print(todolist) # as the list is containing both strings and numbers, so it's called mixed list
# accessing elements from a list
#print(todolist[5])
# print(todolist[8]) # it will give error as it does not have any element corresponding this index in the list we made
#integer list
numbers =[23,35,53,254,55,53,int("322")]
#print(numbers)
#print(numbers.sort()) # will give none as its only sorting the list
#print(numbers)
#numbers.reverse()
#print(numbers)
# slicing also works same way as works in the strings and here in slicing the return type is list like string in strings
#print(numbers[::-3])

# as the third parameter in the slicing goes beyond -1, the result changes , mind it********
#print(len(numbers))
#print(max(numbers))
#print(min(numbers))
#numbers.append(23434) # adds at the end of the list
#print(numbers)
#numbers.insert(3,2343224) # inserts the number at specified position in the list
#print(numbers)
#numbers.pop() # removes an element from the end of the list
#print(numbers)
#numbers.remove(254)  # removes the element that is given in the function
#print(numbers)
#numbers[1]=23432423424
#print(numbers)

# mutable - that can be changed->  list ->elements are written inside square brackets "[]"
# immutabe - that can't be changed-> tuple -> elements are written inside parenthesis "()"
tp=(1,3,5,24,24)
#print(tp)
#tp[2]=42 # will give an error as it's immutable
# for making tuple with single element then we require an extra comma
#tp1=(1) # not an tuple
#print(tp1)
#tp2=(1,) # is an tuple *** remember this
#print(tp2)
a=123
b=3234
# to swap the numbers a and b, will use
a,b=b,a
print(a,b)

