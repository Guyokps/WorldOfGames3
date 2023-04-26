import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Live import load_game, welcome
from Utils import screen_cleaner

welcome()

play_again = "y"

while play_again.lower() == "y":
    user_choices = load_game()

    if user_choices[0] == 2:
        GuessGame.play(user_choices[1])
    elif user_choices[0] == 1:
        MemoryGame.play(user_choices[1])
    elif user_choices[0] == 3:
        CurrencyRouletteGame.play(user_choices[1])

    play_again = input("Do you want to play again? (y/n):\n")

    if play_again.lower() == "y":
        screen_cleaner()
    else:
        print("Thanks for playing!")


