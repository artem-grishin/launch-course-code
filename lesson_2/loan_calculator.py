
def valid_input(prompt):
    while True:
        result = (
            input(prompt)
                .replace('%', '')
                .replace(',', '')
        )
        try:
            if '%' in prompt:
                result = float(result) / 100
            else:
                result = float(result)
            return result
        except ValueError:
            print('Incorrect entry entered, try again.')

def get_monthly_payment(principle, interest, duration):
    monthly_interest = interest / 12
    Duration *= 12 # loan duration in months
    result = principle * (
        monthly_interest / (1 - (1 + monthly_interest) ** (-duration))
    )
    return result


print('Welcome to the Loan Calculator Program.')


while True:

    principle = valid_input('Enter your loan amount: ')
    interest = valid_input('Enter the interest rate as a % (e.g. 5.5%): ')
    duration = valid_input('Enter loan duration in years: ')

    monthly_payment = get_monthly_payment(principle, interest, duration)                          
    print(f'Your monthly payment is ${monthly_payment:,.2f}')

    print('Would you like to make an another loan calculation? (y/n)')
    answer = input()
    if answer and answer[0].lower().startswith('y'):
        continue
    else:
        break
print('\nGoodbye and thank you for using the loan calculator program.\n')  
    

