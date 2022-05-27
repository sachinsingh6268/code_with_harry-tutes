print("**** Let's play a game in which you have 6 chances to guess a number !!!!")
ans=10
remain_guess=6
while remain_guess>0:
    print("You have ",remain_guess," guesse\guesses")
    guessed_number=int(input("Guess the number\n"))
    if guessed_number==ans:
        print("Congratulations, you guessed the correct number!!\n You have taken ",6-remain_guess+1,"guess/guesses to guess the number correctly")
        break
    elif remain_guess!=1:
        if guessed_number<10:
            print("Your number is less than the number to be guessed, please select a greater number\n")
        else:
            print("Your number is greater than the number to be guessed, please select a smaller number\n")
    remain_guess-=1
if(remain_guess==0):
    print("\n\n\n\nGame Over!!!!, You exhausted all the chances to guess")