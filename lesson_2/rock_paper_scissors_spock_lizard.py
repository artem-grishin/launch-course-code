import random
import pdb

def prompt(message: str) -> str:
    print(f'=> {message}')

def get_result(comp_choice: str, user_choice: str) -> str:
    winner = 'tie'
    for key, values in choices_dict[comp_choice].items():
        print(values)
        if user_choice in values:
            if key == 'wins_vs':
                winner = 'Computer'
            elif key == 'loses_to':
                winner = 'User'
    return winner

def display_result(comp_choice: str, user_choice: str, winner: str)-> str:

    prompt(f'Computer chose: {comp_choice}')
    prompt(f'User chose: {user_choice}')

    if winner != 'tie':
        prompt(f'The Winner is {winner}!\n')
    else:
        prompt(f"It's a {winner}!\n")




choices_dict = {
    'rock': {
        'wins_vs': ['scissors', 'lizard'],
        'loses_to': ['paper', 'spock'],
        'winning_action': 'crushes',
    },
    'paper': {
        'wins_vs': ['rock', 'spock'],
        'loses_to': ['scissors', 'lizard'],
        'winning_action': 'covers',
    },
    'scissors': {
        'wins_vs': ['paper', 'lizard'],
        'loses_to': ['rock', 'spock'],
        'winning_action': 'cuts',
    },
    'lizard': {
        'wins_vs': ['paper', 'spock'],
        'loses_to': ['rock', 'scissors'],
        'winning_action': 'poisons',
    },
    'spock': {
        'wins_vs': ['rock', 'scissors'],
        'loses_to': ['lizard', 'paper'],
        'winning_action': 'smashes',
    },
}

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

prompt('Welcome to rock, paper, scissors, lizard, spock!')

play_again = True
while play_again:

    comp_choice = random.choice(VALID_CHOICES)
    user_choice = prompt(f'Please choose from: {", ".join(VALID_CHOICES)}')
    user_choice = input()
    if user_choice.lower() in VALID_CHOICES:
        winner = get_result(comp_choice, user_choice)
        display_result(comp_choice, user_choice, winner)
    else:
        prompt('Incorrect choice, please choose again.')
        continue

    answer = prompt('Would you like to play again? (y/n): ')
    answer = input()
    
    if not answer or answer.lower()[0] == 'n':
        prompt('Thank you for playing. Goodbye!')
        play_again = False
