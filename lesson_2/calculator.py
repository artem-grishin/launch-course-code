import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANG = 'en'    
def messages(LANG, message):
    return MESSAGES[LANG][message]

def prompt(key):
    message = messages(LANG, key)
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('welcome')

while True:

    prompt('ask_first_num')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_num')
        number1 = input()

    prompt('ask_second_num')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_num')
        number2 = input()

    prompt('choose_operation')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("must_choose_num")
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    print(f"=> The result is {output:,.2f}")

    prompt('continue?')
    continue_choice = input()
    if continue_choice and continue_choice[0].lower() != 'y':
        break
    
print('Goodbye and thank you for using the python calculator program!')

