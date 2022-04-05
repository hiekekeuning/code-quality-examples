def place_a_guess(guesses, answer, player_name):
    if guesses > 0:
        print(f"Player {player_name} has {guesses} guesses left")

        guess = int(input("Guess a number"))
        if guess == answer:
            print("You win!")
            return True
        else:
            if guess < answer:
                print("Too low!")
            else:
                print("Too high!")
            return False
    else:
        return True


place_a_guess(5, 3, "Hieke")






def place_a_guess2(guesses, answer, player_name):
    if guesses <= 0:
        return False

    print(f"Player {player_name} has {guesses} guesses left")

    guess = int(input("Guess a number"))
    if guess == answer:
        print("You win!")
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
    return guess == answer


place_a_guess2(5, 3, "Hieke")
