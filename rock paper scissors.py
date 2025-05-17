import random

option = ("rock", "paper", "scissor")
player = None
player_point = 0
computer_point = 0
running = True

while running == True:
    while player not in option:
        player = input("enter a choice: rock , paper , scissor ").lower()
        computer = random.choice(option)

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == "rock" and computer == "paper":
        computer_point += 1
        print("computer wins!")

    elif player == "scissor" and computer == "rock":
        computer_point += 1
        print("Computer wins!")

    elif player == "paper" and computer == "scissor":
        computer_point += 1
        print("Computer wins!")

    elif player == "scissor" and computer == "scissor":
        print("Its a tie!")

    elif player == "rock" and computer == "rock":
        print("Its a tie!")

    elif player == "paper" and computer == "paper":
        print("Its a tie!")

    elif player == "paper" and computer == "rock":
        player_point += 1
        print("player wins!")

    elif player == "scissor" and computer == "paper":
        player_point += 1
        print("Player wins!")

    elif player == "rock" and computer == "scissor":
        player_point += 1
        print("Player wins!")
    game = None
    while game not in ['y', 'n']:
        game = input("play again? (y/n: )").lower()
    if game == "y":
        player = None  # Reset player choice
        continue
    else:
        print(f"Final Score - Player: {player_point}, Computer: {computer_point}")
        running = False






