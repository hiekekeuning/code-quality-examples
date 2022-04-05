def ask_name_and_age_and_check_age():

    while True:
        name = input("Enter your name: ")
        if len(name) <= 1:
            print("Names have more than one character! Try again")
        else:
            break

    while True:
        line = input("Enter your age: ")
        try:
            age = int(line)
            break
        except ValueError:
            print("That's not a number! Try again")

    YOUNG_CUTOFF = 30
    if age <= YOUNG_CUTOFF:
        print(f"{name}, you are young!")
    else:
        print(f"{name}, you are old!")


ask_name_and_age_and_check_age()