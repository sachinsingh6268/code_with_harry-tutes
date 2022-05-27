n=int(input("Enter the height of the tree structure\n"))
# for false we will print the stars in reverse order and for true we will print the stars normal order
order=int(input("Give the order of the printing \n")) # input can be 0 or 1 only
ordertype=None
if order==1:
    ordertype=True
else:
    ordertype=False

if ordertype:
     for i in range(1,n+1):
        print("*"*i)


else:
    for i in range(n,0,-1):
        print("*"*i)




