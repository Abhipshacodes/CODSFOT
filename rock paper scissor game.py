import random

def play_rock_paper_scissors():

    user_wins = 0
    computer_wins = 0

    while True:
        print("\nRock-Paper-Scissors Game!")
        print(f"Your score: {user_wins}, Computer score: {computer_wins}")

        while True:
            user_choice = input("\nChoose rock, paper, or scissors: ").lower()
            if user_choice in ["rock", "paper", "scissors"]:
                break
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            user_wins += 1
            print("You win!")
        else:
            computer_wins += 1
            print("Computer wins!")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_rock_paper_scissors()
