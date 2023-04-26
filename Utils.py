import os
import subprocess
import sys

SCORES_FILE_NAME = 'Scores.txt'

BAD_RETURN_CODE = 0

try:
    with open(SCORES_FILE_NAME, 'r') as file:
        content = file.read()
    # print(content)
except FileNotFoundError as e:
    print("The file does not exist.")
    BAD_RETURN_CODE = e.errno
    print(f"Error number: {BAD_RETURN_CODE}")
except Exception as e:
    print("An error occurred:", e)
    BAD_RETURN_CODE = e.errno
    print(f"Error number: {BAD_RETURN_CODE}")


def screen_cleaner():

    operating_system = sys.platform

    if operating_system == 'win32':
        subprocess.run('cls', shell=True)

    elif operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)

    else:  # macOS and Linux
        os.system('clear')