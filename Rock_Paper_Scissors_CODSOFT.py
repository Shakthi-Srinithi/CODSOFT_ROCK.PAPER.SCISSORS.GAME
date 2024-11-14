import random 

def play_game():
    while True:
        user_choice = input("Choose 'rock', 'paper', or 'scissors': ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. You LOSE :(")
            continue
        
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a TIE!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You WIN :)")
        else:
            print("You LOSE :(")

        if input("Play again? (yes/no): ").lower() != 'yes':
            print("Thanks for Playing! Bubyee :D")
            break

play_game()

