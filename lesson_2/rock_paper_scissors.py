import random


def get_result(comp_choice: str, user_choice: str) -> str:
    # comp = rock
    # user = scissors
    winner = 'tie'
    for key, value in choices_dict[comp_choice].items():
        if user_choice == value and key == 'wins':
            winner = 'Computer'
        elif user_choice == value and key == 'loses':
            winner = 'User'
    return winner

def display_result(comp_choice: str, user_choice: str, winner: str)-> str:

    print(f'\nComputer chose: {comp_choice}')
    print(f'User chose: {user_choice}')

    if winner != 'tie':
        print(f'The Winner is {winner}!\n')
    else:
        print(f"It's a {winner}!\n")
    
        
choices_dict = {
    'rock': {
        'wins': 'scissors',
        'loses': 'paper',
    },
    'paper': {
        'wins': 'rock',
        'loses': 'scissors',
    },
    'scissors': {
        'wins': 'paper',
        'loses': 'rock',
    },
}

comp_choice = random.choice(list(choices_dict.keys())) 
user_choice = random.choice(list(choices_dict.keys()))

winner = get_result(comp_choice, user_choice)
display_result(comp_choice, user_choice, winner)
