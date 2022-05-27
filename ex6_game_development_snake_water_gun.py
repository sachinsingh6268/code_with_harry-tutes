# snake water gun game
import random
list=["Snake","Water","Gun"]
abbr={"s":"Snake","w":"Water","g":"Gun"}
play={"y":True,"n":False}
print("Let's play SNAKE WATER GUN GAME")
print("You will play this game 10 times, To win your score should be more than 50%")
yes="y"
while(play[yes]):
    i=0
    s_won=0
    user_won=0
    while i<10:
        i+=1
        system_choice=random.choice(list)
        user_choice=input("Enter your choice\n** Press s to choose Snake\n** Press w to choose Water\n** Press g to choose Gun\n")
        try:
            if system_choice==user_choice:
                print("You selected the same choice as the system selected, You wasted 1 chance!!!\nPlease try again")
                continue
            if (system_choice=="Snake" and abbr[user_choice]=="Water") or (system_choice=="Gun" and abbr[user_choice]=="Snake") or (system_choice=="Water" and abbr[user_choice]=="Gun"):
                s_won+=1
                if(i==10):
                    print("You loose!!! Sorry you don't have any chance left to play further")
                else:
                    print("You loose!!! You may try again")

            else:
                user_won+=1
                if(i==10):
                    print("Congratulations, You won!!!, now you don't have chance left")
                else:
                    print("Congratulations, You won!!!, play again")
        except Exception as e:
            print("You choosen wrong entry!!!")
    print("\n\n")
    print("Your Score: ",user_won,"\nComputer Score: ",s_won)
    if s_won<user_won:
        print("WELL DONE,YOU WON THE GAME!!!!")
    elif s_won>user_won:
        print("OOPS, YOU LOSE THE GAME!!!!")
    else:
        print("GAME TIED")
    play_again=input("Want to play again: y/n\n")
    yes=play_again