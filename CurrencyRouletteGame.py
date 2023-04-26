import random

from CurrencyConverterAPI import *


def get_money_interval(difficulty, currency_amount_random_generator):
    print('Loading...... might take few seconds')
    correct_result = ils_to_usd_converter(currency_amount_random_generator)

    lower_bound = correct_result - (5 - difficulty)
    upper_bound = correct_result + (5 - difficulty)
    money_interval = (lower_bound, upper_bound)

    return money_interval


def get_guess_from_user(currency_amount_random_generator):
    user_answer = float(input(f'How much in ILS is {currency_amount_random_generator}$?\n'))

    return user_answer


def play(difficulty):
    currency_amount_random_generator = random.randint(1, 100)
    correct_result = ils_to_usd_converter(currency_amount_random_generator)
    result_range = get_money_interval(difficulty, currency_amount_random_generator)

    user_guess = get_guess_from_user(currency_amount_random_generator)

    if result_range[1] >= user_guess >= result_range[0]:
        print('You WON!')

    else:
        print(f'You LOSE\nthe correct answer was {correct_result}')

