import random

def play_cup_game():
    # Computer randomly chooses a cup (1, 2, or 3)
    ball_cup = random.randint(1, 3)
    
    print("\n========== Cup and Ball Game ==========")
    print("The ball is hidden under one of three cups!")
    
    # Get user's guess
    try:
        guess = int(input("Which cup do you think has the ball? (1, 2, or 3): "))
        
        # Validate input
        if guess not in [1, 2, 3]:
            print("Please enter a valid cup number (1, 2, or 3)!")
            return
        
        # Check if guess is correct
        if guess == ball_cup:
            print(f"\nYou got it! The ball was under cup {ball_cup}! 🎉")
        else:
            print(f"\nSorry, the ball was under cup {ball_cup}. Try again!")
            
    except ValueError:
        print("Please enter a valid number!")

def get_play_again_response():
    while True:
        response = input("\nWould you like to play again? (yes/no): ").lower()
        if response in ['yes', 'no']:
            return response
        print("Invalid input! Please enter 'yes' or 'no'.")

# Main game loop
playing = True
while playing:
    play_cup_game()
    
    # Ask if player wants to play again with validation
    play_again = get_play_again_response()
    if play_again == 'no':
        print("\nThanks for playing! Goodbye!")
        playing = False 
        