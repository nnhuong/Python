
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
        game_on = False
    else:
            random_index = random.randint(0,2 )
            computer_choice = choices[random_index]
            
            print(f"You select{get_choice(user_choice)} vs Computer choice is {get_choice(computer_choice)}")
            #winning rules
            if user_choice == "R" and computer_choice == "S":
                print("You win")
            elif user_choice == "P" and computer_choice == "R":
                print("You win")
            elif user_choice == "S" and computer_choice == "P":
                print("You win")
            
            elif user_choice == "R" and computer_choice == "P":
                print("Sorry, you're lose")
            elif user_choice == "P" and computer_choice == "S":
                print("Sorry, you're lose")
            elif user_choice == "S" and computer_choice == "R":
                print("Sorry, you're lose")
                
            elif user_choice == computer_choice:
                print(f"wow, it's a Draw")
            else:
                print('Invalid option: Please enter [R, P, S, Q only]')
    counter +=1
        
if __name__ == "__main__":
    main()