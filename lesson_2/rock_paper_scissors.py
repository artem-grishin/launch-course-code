import random

def prompt(message: str) -> str:
    print(f'=> {message}')

def get_result(comp_choice: str, user_choice: str) -> str:
    winner = 'tie'
    for key, value in choices_dict[comp_choice].items():
        if user_choice == value and key == 'wins':
            winner = 'Computer'
        elif user_choice == value and key == 'loses':
            winner = 'User'
    return winner

def display_result(comp_choice: str, user_choice: str, winner: str)-> str:

    prompt(f'Computer chose: {comp_choice}')
    prompt(f'User chose: {user_choice}')

    if winner != 'tie':
        prompt(f'The Winner is {winner}!\n')
    else:
        prompt(f"It's a {winner}!\n")


# TODO add option to keep playing
# TODO add input for user and check for errors

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

VALID_CHOICES = ['rock', 'paper', 'scissors']

prompt('Welcome to rock, paper, scissors!')

play_again = True
while play_again:

    comp_choice = random.choice(list(choices_dict.keys()))
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
