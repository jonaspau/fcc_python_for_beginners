import random


def main():
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock crushes scissors"
        else:
            return "Paper covers rock"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper"
        else:
            return "Paper covers rock"
    elif player == "scissors":
        if computer == "rock":
            return "Rock crushes scissors"
        else:
            return "Scissors cuts paper"
    else:
        return "Invalid choice"

main()