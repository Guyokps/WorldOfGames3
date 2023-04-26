from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    try:
        with open(SCORES_FILE_NAME, 'r+') as file:
            # Read the first line of the file
            content = file.readline()

            # Print the contents of the file
            # print(content)

            # Check if content is not empty before converting it to int
            if content:
                POINTS_OF_WINNING = int(content) + POINTS_OF_WINNING

            # Move the file pointer to the beginning of the file
            file.seek(0)

            # Write the new value to the file
            file.write(str(POINTS_OF_WINNING))

            # Truncate the remaining content (if any)
            file.truncate()
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open('Scores.txt', 'w') as file:
            file.write(str(POINTS_OF_WINNING))

    print(POINTS_OF_WINNING)


add_score(5)
