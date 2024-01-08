import random

def get_choice(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    else:
        return "Scissor"

def main():
    print("Welcome to our game")
    print("[R] = Rock, [P] = Paper, [S]= Scissor and [Q] = Quit Game")
    
    choices = ["R", "P", "S"]
    counter = 1
    game_on = True
    
    while game_on:
        user_choice = input(f"Game #{counter}. Please enter your choice: ")
        user_choice = user_choice.upper()
        
        if user_choice == "Q":
            print('Thanks for joining. Have a nice day')
            break
        else:
            random_index = random.randint(0, 2)
            computer_choice = choices[random_index]
            
            print(f"You select {get_choice(user_choice)} vs Computer choice is {get_choice(computer_choice)}")
            
            if user_choice == computer_choice:
                print(f"Wow, it's a Draw")
            elif (
                (user_choice == "R" and computer_choice == "S") or
                (user_choice == "P" and computer_choice == "R") or
                (user_choice == "S" and computer_choice == "P")
            ):
                print("You win")
            else:
                print("Sorry, you lose")
        
        counter += 1

if __name__ == "__main__":
    main()
