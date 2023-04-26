import random
import time


def play(difficulty):
    system_generated_list = generate_sequence(difficulty)
    print(system_generated_list, end="")
    time.sleep(0.7)
    print("", end="\r")

    user_answer = get_list_from_user(difficulty)
    is_equal = is_list_equal(system_generated_list, user_answer)
    if is_equal:
        print('WIN! You guessed all the numbers')
    else:
        print('LOSE, You did not guess correctly the numbers')


def generate_sequence(difficulty):
    system_generated_list = []
    for i in range(difficulty):
        random_num = random.randint(1, 101)
        system_generated_list.append(random_num)
    return system_generated_list


def get_list_from_user(difficulty):
    user_answer = []
    for i in range(difficulty):
        print(f'Insert your answer number {i + 1}')
        message = int(input())
        user_answer.append(message)
    return user_answer


def is_list_equal(system_generated_list, user_answer):
    if system_generated_list == user_answer:
        return True
    else:
        return False
