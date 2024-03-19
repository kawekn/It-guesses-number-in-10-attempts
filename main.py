
def tryme():
    min_possible = 0
    max_possible = 1000
    print("thin about two numbers between 0 and 1000")
    while True:
        guess = int((max_possible-min_possible) / 2) + min_possible
        print(f"My guess is {guess}")
        hint = input(print(f"Tell me is it: too big / too small / correct"))
        if hint == "correct":
            print(f"It was {guess}, I win")
            break
        elif hint == "too big":
            max_possible = guess
        elif hint == "too small":
            min_possible = guess


tryme()
