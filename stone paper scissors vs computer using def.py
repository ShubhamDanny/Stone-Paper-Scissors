import random
while True:

    user_choice = int(input("1 for stone \n2 for paper \n3 for scissors \nPlease enter your choice: "))

    if user_choice > 3 or user_choice < 1: # Error message
        print('Please enter the input correctly')
        exit()

    if user_choice == 1:
        user_choice = 'stone'
    elif user_choice == 2:
        user_choice = 'paper'
    elif user_choice == 3:
        user_choice = 'scissors'

    choices = ('stone', 'paper', 'scissors')
    choice = random.randint(1,3)
    comp_choice = choices[choice]

    print(f"Your choice is {user_choice} and computer's choice is {comp_choice}\nIt's {user_choice} VS {comp_choice} ")

    if comp_choice == user_choice:
        print("Both wins")

    elif comp_choice == 'stone' and user_choice == 'paper':
        print('You won!')
    elif comp_choice == 'paper' and user_choice == 'scissors':
        print('You won!')
    elif comp_choice == 'scissors' and user_choice == 'stone':
        print('You won!')
    else :
        print('You lose!')

    again = input("do you want to play again?  (y/n) ")
    if again.lower() == 'y':
        continue
    else :
        break