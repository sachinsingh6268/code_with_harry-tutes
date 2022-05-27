# function to get the date
client_list={1:"Sachin",2:"Anuj",3:"Sahil"}
e_f_list={1:"exercise",2:"food"}
def getdate():
    import datetime
    return datetime.datetime.now()

# fuction to write the data
def writedata(client_no,exer_or_food,addthis):
    f=open(client_list[client_no]+"_"+e_f_list[exer_or_food]+".txt","at")
    f.write(str([str(getdate())])+"  :  "+addthis+"\n")
    f.close()

def getdata(client_no,exer_or_food):
    f=open(client_list[client_no]+"_"+e_f_list[exer_or_food]+"file.txt")
    data=f.read()
    return data

# there are 3 clients in this health management system
# press 1 for Sachin,2 for Anuj, 3 for Sahil
print("****** We have 3 clients here ******\n")

q=1
while(q):
    try:
        print("Want to log or retrieve the data?\nPress 1 for retrieving\nPress 2 to log the information")
        log_or_ret = int(input())
        if(log_or_ret==2):
            print("press 1 for Sachin\npress 2 for Anuj\npress 3 for Sahil")
            client_no = int(input())
            exer_or_food=int(input("Press 1 to log exercise\nPress 2 to log food\n"))
            addthis=input("What you want to add in the health management system for the selected client\n")
            writedata(client_no,exer_or_food,addthis)
            print("you have successfully added: ",addthis)
        else:
            print("Press 1 for Sachin\nPress 2 for Anuj\nPress 3 for Sahil")
            client_no=int(input())
            exer_or_food=int(input("Press 1 to get exercise info\nPress 2 to get food info\n"))
            print("data successfully retrieved is:\n",getdata(client_no,exer_or_food))
    except Exception as e:
        print("You have no information to retrieve, Please first log something first")

    q=int(input("\n\nPress 1 to continue\nPress 0 to exit from the Health management system\n"))
