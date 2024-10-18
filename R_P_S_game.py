import random
player_name=input("enter player name:").capitalize() # Player name
user_count=0
computer_count=0
tie_count =0
options=['rock','paper','scissors']
while True:
    user_input=input("enter your options rock/paper/scissors or Q for Quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_input=random.randint(0,2)
    computer_pick=options[random_input]
    # 0 : rock , 1 : paper, 2 : scissors
    print("computer_picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors" :
        print(" Rock smashes scissors ---> You Won!")
        user_count+=1
    elif user_input == "scissors" and computer_pick == "paper":
        print(" scissors cut paper --> You Won!")
        user_count +=1
    elif user_input == "paper" and computer_pick == "rock":
        print(" paper cover rock --> You Won!")
        user_count +=1
    elif user_input == computer_pick: # both picks same then it's tie!
        tie_count +=1
        print("It's a tie!")
        user_input1=input(" Try again! Yes/No ").lower()
        if user_input1 !="yes":
            break
    else:
        print("You Lost!")
        computer_count +=1

print(player_name,"won=", user_count)
print("Computer won =",computer_count)
print("tie count =",tie_count)
print("BYE!")


