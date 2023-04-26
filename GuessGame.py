import random


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    final_answer = compare_results(secret_number, guess)

    if final_answer:
        print('You Won')
    else:
        print('You Lost')

    print(f'You guessed {guess}, and the secret number was {secret_number}')


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    print(f'Please guess a number between 1 to {difficulty}')
    while True:
        try:
            guess = int(input())
            if guess < 1 or guess > difficulty:
                print(f'Please guess a number between 1 to {difficulty}')
            else:
                return guess
        except ValueError:
            print(f'Please guess a number between 1 to {difficulty}')


def compare_results(secret_number, guess):
    if secret_number == guess:
        return True
    else:
        return False
