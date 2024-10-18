import random
player_name=input("enter player name:").capitalize()
user_count=0
computer_count=0
options=['rock','paper','scissor']
while True:
    user_input=input("enter your options rock/paper/scissor or Q for Quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_input=random.randint(0,2)
    computer_pick=options[random_input]
    print("computer_picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor" :
        print("You Won!")
        user_count+=1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_count +=1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_count +=1
    else:
        print("You Lost!")
        computer_count +=1

print(player_name,"won=", user_count)
print("Computer won =",computer_count)
print("BYE!")


