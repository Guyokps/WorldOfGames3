# Welcomes the user input and prints a simple string
def welcome():
    print('Please enter your name')
    user_name = input()
    print(f'Hello {user_name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.\n')


# User choosing game and prints his decision, strings and float numbers are handled
def load_game():
    print(f'Please choose a game to play:\n '
          f'1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n '
          f'2. Guess Game - guess a number and see if you chose like the computer\n '
          f'3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n')

    user_chosen_game = input()
    while not user_chosen_game.isdigit() or int(user_chosen_game) < 1 or int(user_chosen_game) > 3:
        print('Please enter a number between 1 ~ 3')
        user_chosen_game = input()
    try:
        user_chosen_game = int(user_chosen_game)
        if user_chosen_game == 1:
            print('You chosen game 1')
        elif user_chosen_game == 2:
            print('You chosen game 2')
        elif user_chosen_game == 3:
            print('You chosen game 3')
        print('\n')
    except ValueError:
        print('Please enter a number between 1 to 3.')

    # User choosing difficulty with integers only between 1 and 5, float and strings are handled
    print('Please choose game difficulty from 1 to 5:')
    while True:
        try:
            user_difficulty = int(input())
            if user_difficulty < 1 or user_difficulty > 5:
                print('Please choose a difficulty between 1 to 5')
            else:
                break
        except ValueError:
            print('Please choose a number between 1 to 5')

    if user_difficulty == 1:
        print('You chose difficulty 1')
    elif user_difficulty == 2:
        print('You chose difficulty 2')
    elif user_difficulty == 3:
        print('You chose difficulty 3')
    elif user_difficulty == 4:
        print('You chose difficulty 4')
    elif user_difficulty == 5:
        print('You chose difficulty 5')

    user_choices = [user_chosen_game, user_difficulty]
    return user_choices
