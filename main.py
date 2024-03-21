
def tryme():
    """
        A simple number guessing game.

        The program guesses the user's number between 0 and 1000.
        The user provides feedback ('too big', 'too small', or 'correct') for each guess.
        """
    min_possible = 0
    max_possible = 1000
    input("thin about a number in range from 0 to 1000 and press Enter when You are ready.")
    while True:
        guess = int((max_possible-min_possible) // 2) + min_possible
        print(f"My guess is {guess}")
        hint = input(f"Tell me is it: too big / too small / correct : ")
        if hint == "correct":
            print(f"It was {guess}, I win")
            break
        elif hint == "too big":
            max_possible = guess - 1
        elif hint == "too small":
            min_possible = guess + 1


tryme()
