valid_choices = ["1", "2", "3", "4",
                 "coin flip", "cha hon", "roulette", "quit"]


def choices():
    print("\nWhat would you like to play?")
    print("1. Coin flip")
    print("2. Cha Hon")
    print("3. Roulette")
    print("4. Quit")
    print("\n")

    choice = input("enter your choice here: >")

    if choice.lower() in str(valid_choices[0]) or choice.lower() in valid_choices[4]:
        coin_flip()
    elif choice.lower() in valid_choices[1] or choice.lower() in valid_choices[5]:
        cha_hon()
    elif choice.lower() in valid_choices[2] or choice.lower() in valid_choices[6]:
        roulette()
    elif choice.lower() in valid_choices[3] or choice.lower() in valid_choices[7]:
        sys.exit()
    else:
        print("Please enter a valid choice: ")
        choices()


choices()
