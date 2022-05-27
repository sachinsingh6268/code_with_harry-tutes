# what are enumerate functions and how they make our coding journey easy and simple

# let's understand with an example
# below are the games that Sahil likes to play
l1=["Cricket","Football","Kabaddi","Kho-Kho","Hide & Seek","BasketBall"]
# Now today Sahil has only choice to play the games that are in the odd places in the list and he asked Arpit to give him the list as soon as possibe
# Now Arpit uses a naive approach as below
# i=1
# for item in l1:
#     if(i%2!=0):
#         print(item)
#     i+=1



# It gives the required result but Arpit need to maintain an extra variable i for this,, he heard from a friend that enumerate function can make his work quite easy
# So let's discuss the solution with help of enumerate function

for index,item in enumerate(l1):  # enumerate gives both index(value starting from 0) and item
    if index%2==0:
        print(f"Sahil will play today {item}")

# here in enumerate function we need not to maintain any variable explcitly, enumerate function takes care of it
