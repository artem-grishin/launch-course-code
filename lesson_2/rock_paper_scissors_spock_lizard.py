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
        'shortened_name': 'r',
    },
    'paper': {
        'wins_vs': ['rock', 'spock'],
        'loses_to': ['scissors', 'lizard'],
        'winning_action': 'covers',
        'shortened_name': 'p',        
    },
    'scissors': {
        'wins_vs': ['paper', 'lizard'],
        'loses_to': ['rock', 'spock'],
        'winning_action': 'cuts',
        'shortened_name': 'sc',        
    },
    'lizard': {
        'wins_vs': ['paper', 'spock'],
        'loses_to': ['rock', 'scissors'],
        'winning_action': 'poisons',
        'shortened_name': 'l',        
    },
    'spock': {
        'wins_vs': ['rock', 'scissors'],
        'loses_to': ['lizard', 'paper'],
        'winning_action': 'smashes',
        'shortened_name': 'sp',        
    },
}


prompt('Welcome to rock, paper, scissors, lizard, spock!')

match_count = 0
while match_count <= 5:

    comp_choice = random.choice(list(choices_dict.keys()))
    
    user_choice = prompt('Please choose from: ')
    for item in zip(choices_dict.keys(), choices_dict.values()):
        item_1 = item[0]
        item_2 = item[1]['shortened_name']
        prompt(f'\t{item_1} => type "{item_2}"')
    user_choice = input()

    name_match = False
    for key, value in choices_dict.items():
        short_name = choices_dict[key]['shortened_name']
        if user_choice == short_name or user_choice == key:
            user_choice = key
            name_match = True
            break

    if name_match:
        winner = get_result(comp_choice, user_choice)
        display_result(comp_choice, user_choice, winner)
    else:
        prompt('Incorrect choice, please choose again.')
        continue

    # answer = prompt('Would you like to play again? (y/n): ')
    # answer = input()
    
    # if not answer or answer.lower()[0] == 'n':
    #     prompt('Thank you for playing. Goodbye!')
    #     play_again = False

    match_count += 1

prompt('\n\nGame Over.\nThank you for playing!\n')
