import os
import random
import msvcrt
from colors import bcolors

# Symbols
symbols = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

# Rules
rules = {
    'r': {'s': 'wins', 'p': 'loses', 'r': 'draw'},
    's': {'p': 'wins', 'r': 'loses', 's': 'draw'},
    'p': {'r': 'wins', 's': 'loses', 'p': 'draw'}
}

# Signs
hand_images = {
    'r': """
    ___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    'p': """
     ___
---'    __)__
           ______)
          _______)
         _______)
---.__________)
""",
    's': """
    ___
---'   __)__
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Match score
player_score = 0
computer_score = 0
games_played = 0
consecutive_wins = 0
consecutive_losses = 0

# Different phrases 
win_phrases = [
    "You are such a big brain! Win!",
    "Victory is sweet, and it's all yours!",
    "You're on fire! Another win for you!",
]

loss_phrases = [
    "Someone's having a bad day today...You lose",
    "Ouch, that must hurt! Better luck next time!",
    "The computer was just lucky this time!",
]

consecutive_win_phrases = [
    "Three in a row! You're a rockstar!",
    "Hat-trick hero! Keep it up!",
    "Unstoppable! Who can challenge you now?"
]

consecutive_loss_phrases = [
    "Three losses in a row... Is the AI taking over?",
    "Don't give up! Even the best have bad days.",
    "It's just a setback. You'll rise again!"
]

# Def for instructions
def print_instructions():
    print("Welcome to the 'Rock, Paper, Scissors' game!")
    print("Choose your action:")
    for key, value in symbols.items():
        print(f"{key} for {value}")
    print("Press 'q' to exit the game.")

# Player choice
def get_player_choice():
    while True:
        choice = msvcrt.getwch() 
        if choice in symbols:
            return choice
        elif choice == 'q':
            print("Exiting the game.")
            exit()
        else:
            print("Invalid choice. Please choose again.")

# Computer choice
def get_computer_choice():
    return random.choice(list(symbols.keys()))

# Game
def play_game():
    global player_score, computer_score, games_played, consecutive_wins, consecutive_losses
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = rules[player_choice][computer_choice]
    games_played += 1
    os.system('cls')
    
    print("You chose:")
    print(hand_images[player_choice])
    print("Computer chose:")
    print(hand_images[computer_choice])

    # Winner
    if result == 'wins':
        player_score += 1
        consecutive_wins += 1
        consecutive_losses = 0
        print(bcolors.GREEN + random.choice(win_phrases) + bcolors.DEFAULT)
        if consecutive_wins == 3:
            print(bcolors.YELLOW + random.choice(consecutive_win_phrases) + bcolors.DEFAULT)
    elif result == 'loses':
        computer_score += 1
        consecutive_losses += 1
        consecutive_wins = 0
        print(bcolors.RED + random.choice(loss_phrases) + bcolors.DEFAULT)
        if consecutive_losses == 3:
            print(bcolors.PURPLE + random.choice(consecutive_loss_phrases) + bcolors.DEFAULT)
    else:
        consecutive_wins = 0
        consecutive_losses = 0
        print("It's a draw!")

    # Score
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Total games played: {games_played}")

# Game loop
os.system('cls')
print_instructions()
while True:
    play_game()
