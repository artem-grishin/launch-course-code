import random

# Declare dictionaries and variables

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

scores_dict = {
    'Computer': 0,
    'User': 0,
    'tie': 0,
}

match_count = 0
# Define functions

def prompt(message: str) -> str:
    print(f'=> {message}')

def get_match_result(comp_choice: str, user_choice: str) -> str:
    match_winner = 'tie'
    for key, value in choices_dict[comp_choice].items():
        if user_choice in value:
            if key == 'wins_vs':
                match_winner = 'Computer'
            elif key == 'loses_to':
                match_winner = 'User'
    return match_winner

def display_match_result(comp_choice: str, user_choice: str, match_winner: str)-> str:

    prompt(f'Computer chose: {comp_choice}')
    prompt(f'User chose: {user_choice}')

    if match_winner != 'tie':
        prompt(f'The winner is {match_winner}!\n')
    else:
        prompt(f"It's a {match_winner}!\n")

def check_for_grand_winner(scores_dict: dict) -> str:

    comp_score = scores_dict['Computer']
    user_score = scores_dict['User']
    
    if comp_score == 3:
        grand_winner = 'Computer'
    elif user_score == 3:
        grand_winner = 'User'
    else:
        grand_winner = ''
        
    return grand_winner

def display_final_result(scores_dict, match_count, grand_winner):
    


    print(f'The computer scored {scores_dict['Computer']} win(s).')
    print(f'The user scored {scores_dict['User']} win(s).')
    print(f'There were {scores_dict['tie']} ties.\n')
    
    if grand_winner and match_count < 5:
        print(f'\nThe match ended early since 3 wins were reached.\
        after {match_count} matches.\n\n\
        The grand winner is {grand_winner}!\n')
    else:
        # highest_score = max(scores_dict['Computer'], scores_dict['User'])
        # grand_winner = ''
        highest_score = 0
        for key, value in scores_dict.items():
            if value > highest_score:
                highest_score = value
                grand_winner = key
                
        if highest_score == 0:
            print('The final result is a tie!')
        else:
            print(f'After {match_count} matches.\
            \nThe grand winner is {grand_winner}!.\n')

prompt('Welcome to rock, paper, scissors, lizard, spock!')

while match_count < 5:

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
        match_winner = get_match_result(comp_choice, user_choice)
        scores_dict[match_winner] += 1

        display_match_result(comp_choice, user_choice, match_winner)
        match_count += 1

        if match_count < 5:
            grand_winner = check_for_grand_winner(scores_dict)
            if grand_winner != '':
                break
    else:
        prompt('Incorrect choice, please choose again.')
        continue

print('Final Result:\n-----------------')
display_final_result(scores_dict, match_count, grand_winner)
prompt('\n\nGame Over.\nThank you for playing!\n')
