from random import *
import cmd
import textwrap
import sys
import os
import time
import pickle
from io import TextIOWrapper
sys.stdout = TextIOWrapper(
    sys.stdout.buffer, encoding='UTF-8', errors='replace')

global player


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100


player = Player("Default")

valid_choices = ["1", "2", "3", "4", "5", "6",
                 "coin flip", "cha hon", "roulette", "save game", "load game", "quit"]
play_again_list = ["yes", "no"]

# for character in greeting:
#    sys.stdout.write(character)
#    sys.stdout.flush()
#    time.sleep(0.05)


def title_screen():
    valid_choices = ["1", "2", "3", "new game", "load game", "exit game"]
    print("Welcome to the Casino! Leave hope at the entrance...")
    print("\n")
    print("1. New game")
    print("2. Load Game")
    print("3. Exit Game")
    choice = input("Make your choice, traveller! :-> ").lower()

    if choice in valid_choices[0] or choice in valid_choices[3]:

        new_game()
    elif choice in valid_choices[1] or choice in valid_choices[4]:
        load_game()
    elif choice in valid_choices[2] or choice in valid_choices[5]:
        sys.exit()
    else:
        print("Please enter a valid choice, traveller!")
        title_screen()


def new_game():

    inp_name = input("What is your name, traveller? :-> ")
    player.name = inp_name
    greeting = "\nHello, {name}, you have travelled from far away to join our merry Casino! \nThe ocean is weary and tired tonight, so come on in and enjoy a glass of whiskey! \n\n<{name} goes inside, looking quite tired.> \n<He sips from the whiskey the waiter serves him.> \n\nOh, there you are! Garcon! His raincoat, please! Never can get enough help these days. ".format(
        name=player.name)
    choices()


def choices():

    print("\n\nWhat would you like to play?")
    print("1. Coin flip")
    print("2. Cha Hon")
    print("3. Roulette")
    print("4. Save Game")
    print("5. Load Game")
    print("6. Quit")
    print("\n")
    print("Current balance: " + str(player.money) + "$ ")
    choice = input("enter your choice here: :-> ")
    if choice.lower() in valid_choices[0] or choice.lower() in valid_choices[6]:
        coin_flip()
    elif choice.lower() in valid_choices[1] or choice.lower() in valid_choices[7]:
        cha_hon()
    elif choice.lower() in valid_choices[2] or choice.lower() in valid_choices[8]:
        roulette()
    elif choice.lower() in valid_choices[3] or choice.lower() in valid_choices[9]:
        save_game()
    elif choice.lower() in valid_choices[4] or choice.lower() in valid_choices[10]:
        load_game()
    elif choice.lower() in valid_choices[5] or choice.lower() in valid_choices[11]:
        sys.exit()
    else:
        print("Please enter a valid choice: ")
        choices()


def save_game():
    save_name = input("Enter save game name: :-> ").lower()

    pickle.dump(player, open("%s.sav" % save_name, "wb"))
    choices()


def load_game():
    global player
    load_name = input("Enter saved game you wish to load: :-> ").lower()

    player = pickle.load(open("%s.sav" % load_name, "rb"))
    choices()


def update():
    quotes_alive = {
        1: "The gods of old are watching over you, traveller...",
        2: "Mercury be praised! {}, aim true towards the sky!".format(player.name),
        3: "Athena is not your patron goddess, that's for sure, {}.".format(player.name)
    }
    quotes_dead = {
        1: "O dread, destitute and poor you must leave this holy sanctuary...",
        2: "The joke the gods played on you was rather cruel...",
        3: "Bleah! Begone infidel, never to return!"
    }
    random_quote = randint(1, 3)

    if player.money > 0:
        print("A wing herald comes down from the ceiling, loudly proclaiming: \n" +
              quotes_alive[random_quote])
        print("You have {} $ left!".format(player.money))

    if player.money <= 0:
        print("A wing herald comes down from the ceiling, loudly proclaiming: \n" +
              quotes_dead[random_quote])
        sys.exit()


def bet_amnt():
    while True:
        try:
            bet_amount = abs(
                int(input("{}, place your bet :-> ".format(player.name))))
            if bet_amount > player.money:
                print("Can't afford that, suga' daddy!")
            else:
                break
        except ValueError:
            print("Please please use whole numbers!")
    return bet_amount


def coin_flip():
    while (player.money > 0):

        bets = {
            "heads": 0,
            "tails": 1
        }
        print("Playing coin flip!")
        guess = input("What's your guess? heads / tails: ").lower()
        if guess in "heads":
            guess = "heads"
        elif guess in "tails":
            guess = "tails"
        else:
            print("Please enter a valid choice, {}".format(player.name))
            coin_flip()
        try:
            bet = int(
                input("What amount are you wagering on that wild guess? $$$ "))
        except ValueError:
            print("We take only whole numbers, {}, we are dreadfuly sorry.".format(
                player.name))
            coin_flip()

        if bet <= player.money:
            lucky = randint(0, 1)
            if lucky == 0:
                print("The coin flipped tails.")
            else:
                print("The coin flipped heads.")

            if bets[guess] == lucky:
                player.money += int(bet)
                print("Congratz, " + player.name + ", you win!")
                print(player.name + ", you have a grand total of " +
                      str(player.money) + "$!")
            else:

                player.money -= int(bet)
                print("Darn, " + player.name + ", you lose!")
                print(player.name + ", you have " +
                      str(player.money) + "$ left!")
            update()

            play_again(coin_flip)

        else:
            print("You can't afford that, " + player.name)
            choices()
    else:
        print("All broke lad, sorry!")
        sys.exit()


def cha_hon():
    function = cha_hon
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    card_dict = {
        1: '2 \u2663',
        2: '2 \u2666',
        3: '2 \u2665',
        4: '2 \u2660',
        5: '3 \u2663',
        6: '3 \u2666',
        7: '3 \u2665',
        8: '3 \u2660',
        9: '4 \u2663',
        10: '4 \u2666',
        11: '4 \u2665',
        12: '4 \u2660',
        13: '5 \u2663',
        14: '5 \u2666',
        15: '5 \u2665',
        16: '5 \u2660',
        17: '6 \u2663',
        18: '6 \u2666',
        19: '6 \u2665',
        20: '6 \u2660',
        21: '7 \u2663',
        22: '7 \u2666',
        23: '7 \u2665',
        24: '7 \u2660',
        25: '8 \u2663',
        26: '8 \u2666',
        27: '8 \u2665',
        28: '8 \u2660',
        29: '9 \u2663',
        30: '9 \u2666',
        31: '9 \u2665',
        32: '9 \u2660',
        33: '10 \u2663',
        34: '10 \u2666',
        35: '10 \u2665',
        36: '10 \u2660',
        37: '14 \u2663',
        38: '14 \u2666',
        39: '14 \u2665',
        40: '14 \u2660',
        41: '12 \u2663',
        42: '12 \u2666',
        43: '12 \u2665',
        44: '12 \u2660',
        45: '13 \u2663',
        46: '13 \u2666',
        47: '13 \u2665',
        48: '13 \u2660',
        49: '11 \u2663',
        50: '11 \u2666',
        51: '11 \u2665',
        52: '11 \u2660'
    }
    print("Playing Cha Hon")

    try:
        bet = int(
            input("What amount of $ are you wagering on this most simple card game? :-> "))
    except ValueError:
        print("We take only whole numbers, {}, we are dreadfuly sorry.".format(
            player.name))
        cha_hon()

    if bet > player.money:
        print("You can't afford that, {}".format(player.name))
        cha_hon()

    while card_list:
        player_card = choice(card_list)
        card_list.remove(player_card)
        enemy_card = choice(card_list)
        card_list.remove(enemy_card)
        time.sleep(2)
        print("Your card is: {}".format(card_dict[player_card]))
        print("\n")

        print("The enemy card is: {}".format(card_dict[enemy_card]))

        if player_card > enemy_card:
            player.money += bet
            print("\n")
            print("Wow, you have won {} $!".format(bet))
        else:
            player.money -= bet
            print("\n")
            print("Sadly you have lost {} $. Better luck next time!".format(bet))

        update()
        play_again(function)

    choices()


def play_again(function):

    while True:
        play_again_str = input("Would you like to play again? :-> ")
        if play_again_str in play_again_list[0] or play_again_str in play_again_list[1]:
            break
    if play_again_str in play_again_list[0]:
        function()
    elif play_again_str in play_again_list[1]:
        choices()
    else:
        play_again(function)


def roulette():
    roulette_nums = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30,
                     8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    io_bets = ["1", "2", "inside bet", "outside bet"]
    i_bets = ["1", "2", "3", "4", "5", "6", "7", "straight",
              "split", "street", "corner", "double street", "trio", "first four"]
    o_bets = ["1", "2", "3", "4", "5", "6", "low or high", "red or black",
              "even or odd", "dozen bet", "column bet", "snake bet"]
    straight = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    h_or_v = ["horizontal", "vertical"]

    inv_vert_split = [34, 35, 36]

    dozens = ["1st dozen", "2nd dozen", "3rd dozen,",
              "first dozen", "second dozen", "third dozen"]

    print("Playing roulette...")
    print("What type of bet would you favor?")
    print("1. Inside bet")
    print("2. Outside bet")
    while True:
        player_choice = input(":-> ").lower()
        try:
            if player_choice in io_bets[0] or player_choice in io_bets[1]:
                break
            elif player_choice in io_bets[2] or player_choice in io_bets[3]:
                break
            elif player_choice in io_bets[4]:
                break
        except IndexError:
            print("Choose something from the list, please!")

    if player_choice in io_bets[0] or player_choice in io_bets[2]:
        print(player.name + ", you are going for an inside bet! Most luck to you! ")
        print("1. Straight")
        print("2. Split")
        print("3. Street")
        print("4. Corner")
        print("5. Double Street")
        print("6. Trio")
        print("7. First four")
        while True:
            player_choice = input(
                "Choose your final bet type :-> ").lower()
            try:
                if player_choice in i_bets[0] or player_choice in i_bets[7]:
                    break
                elif player_choice in i_bets[1] or player_choice in i_bets[8]:
                    break
                elif player_choice in i_bets[2] or player_choice in i_bets[9]:
                    break
                elif player_choice in i_bets[3] or player_choice in i_bets[10]:
                    break
                elif player_choice in i_bets[4] or player_choice in i_bets[11]:
                    break
                elif player_choice in i_bets[5] or player_choice in i_bets[12]:
                    break
                elif player_choice in i_bets[6] or player_choice in i_bets[13]:
                    break

            except IndexError:
                print("Enter something from the list above!")

        if player_choice in i_bets[0] or player_choice in i_bets[7]:
            while True:
                try:

                    bet_choice = int(
                        input("Enter a number from 0 to 36 :-> "))
                    if bet_choice in straight:
                        break

                except ValueError:
                    print("Whole numbers please!")

            bet_amount = bet_amnt()

            lucky = choice(roulette_nums)
            print("Fortuna yelded lucky number: " + str(lucky))
            if bet_choice == lucky:
                print("Congratz! You have won!")
                player.money += bet_amount

            else:
                print("Sorry mate, you have lost! Better luck next time! ")
                player.money -= bet_amount

            update()
            play_again(roulette)

        if player_choice in i_bets[1] or player_choice in i_bets[8]:
            print("Trouble? Make it Double! ")
            while True:
                player_choice = input("Horizontal or Vertical? :-> ")
                try:
                    if player_choice in h_or_v[0] or player_choice in h_or_v[1]:
                        break
                except IndexError:
                    print("Please choose between Horizontal and Vertical splits!")
            if player_choice in h_or_v[0]:
                print("You have chosen a horizontal split. ")
                print("Make your bet!")
                while True:
                    try:

                        bet_choice = int(
                            input("Enter your first number from 1 to 35 :-> "))
                        if bet_choice % 3 == 0:
                            print(
                                "Invalid choice, no split possible with that number...")
                        elif bet_choice < 1 or bet_choice > 35:
                            print(
                                "Invalid choice, no split possible with that number...")
                        else:
                            betting_group = [bet_choice, bet_choice + 1]
                            print("Your horizontal split is " +
                                  str(betting_group))
                            break

                    except ValueError:
                        print("Whole numbers please!")

                bet_amount = bet_amnt()

                lucky = choice(roulette_nums)
                print("Fortuna yelded lucky number: " + str(lucky))

                if lucky in betting_group:

                    print("Congratz! You have won!")
                    player.money += bet_amount

                else:
                    print("Sorry mate, you have lost! Better luck next time! ")
                    player.money -= bet_amount

                update()
                play_again(roulette)

            if player_choice in h_or_v[1]:
                print("You have chosen a vertical split. ")
                print("Make your bet!")

                while True:

                    try:

                        bet_choice = int(
                            input("Enter your first number from 1 to 33 :-> "))
                        if bet_choice in inv_vert_split:
                            print(
                                "Invalid choice, no vertical split possible with that number...")
                        elif bet_choice < 1 or bet_choice > 33:
                            print(
                                "Invalid choice, no vertical split possible with that number...")
                        else:
                            betting_group = [bet_choice, bet_choice + 3]
                            print("Your vertical split is " +
                                  str(betting_group))
                            break

                    except ValueError:
                        print("Whole numbers please!")

                bet_amount = bet_amnt()

                lucky = choice(roulette_nums)
                print("Fortuna yelded lucky number: " + str(lucky))

                if lucky in betting_group:

                    print("Congratz! You have won!")
                    player.money += bet_amount

                else:
                    print("Sorry mate, you have lost! Better luck next time! ")
                    player.money -= bet_amount

                update()
                play_again(roulette)

        if player_choice in i_bets[2] or player_choice in i_bets[9]:
            print("There are some mean streets out there, " + player.name)
            print("Make your bet!")
            while True:
                try:
                    player_choice = int(
                        input("Enter a number from your street :-> "))
                    if player_choice < 1 or player_choice > 36:
                        print("Please enter a valid number, from 1 to 36")

                    elif player_choice % 3 == 0:
                        betting_group = [player_choice - 2,
                                         player_choice - 1, player_choice]
                        break

                    elif player_choice % 3 == 1:
                        betting_group = [player_choice,
                                         player_choice + 1, player_choice + 2]
                        break

                    elif player_choice % 3 == 2:
                        betting_group = [
                            player_choice - 1, player_choice, player_choice + 1]
                        break
                except ValueError:
                    print("We need a whole number for this, sir!")
            print("Your bet is " + str(betting_group))

            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number " + str(lucky) + "!")
            if lucky in betting_group:
                print("Congratz! You have won!")
                player.money += bet_amount
            else:
                print("Ouch! You have lost!")
                player.money -= bet_amount

            update()
            play_again(roulette)

        if player_choice in i_bets[3] or player_choice in i_bets[10]:
            print("Wow, there are some tight corners coming up!")
            print("Make your bet!")
            while True:
                try:
                    print("Choose the top left corner of your square:")
                    player_choice = int(input("Numbers 1 to 32: "))
                    if player_choice < 1 or player_choice > 32:
                        print("We need a valid number, sir")
                    elif player_choice % 3 == 0:
                        print("Please choose the top left corner, sir")
                    else:
                        betting_group = [
                            player_choice, player_choice + 1, player_choice + 3, player_choice + 4]
                        break
                except ValueError:
                    print("We need a whole number, sir!")

            print("Your bet is " + str(betting_group))
            print("If you changed your mind, just bet 0!")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna chose the number " + str(lucky))
            if lucky in betting_group:
                print("Congratz, you have won!")
                player.money += bet_amount
            else:
                print("Darn! Better luck next time!")
                player.money -= bet_amount
            update()
            play_again(roulette)

        if player_choice in i_bets[4] or player_choice in i_bets[11]:
            print("Some day your domain will cover two whole streets!")
            print("Make your bet!")
            while True:
                try:
                    print("Choose a number from your top street.")
                    player_choice = int(input("Numbers 1-33 "))
                    if player_choice < 1 or player_choice > 33:
                        print("Please enter a valid number!")
                    elif player_choice % 3 == 0:
                        betting_group = [player_choice - 2, player_choice - 1, player_choice,
                                         player_choice + 1, player_choice + 2, player_choice + 3]
                        break
                    elif player_choice % 3 == 2:
                        betting_group = [player_choice - 1, player_choice, player_choice +
                                         1, player_choice + 2, player_choice + 3, player_choice + 4]
                        break
                    elif player_choice % 3 == 1:
                        betting_group = [player_choice, player_choice + 1, player_choice +
                                         2, player_choice + 3, player_choice + 4, player_choice + 5]
                        break
                except ValueError:
                    print("We need a whole number, sir!")

            print("Your bet is on " + str(betting_group))
            print("To change your mind, just bet 0!")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:
                print("Heaven smiles down on you!")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount

            update()
            play_again(roulette)

        if player_choice in i_bets[5] or player_choice in i_bets[12]:
            print("Betting on a trio is simple! Good luck!")
            betting_group = [0, 1, 2]
            print("You bet on the following " + str(betting_group))
            print("To change your mind, just bet 0!")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:
                print("That trio worked for you!")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount

            update()
            play_again(roulette)

        if player_choice in i_bets[6] or player_choice in i_bets[13]:
            print("Betting on a bascket is simple! Good luck!")
            betting_group = [0, 1, 2, 4]
            print("You bet on the following " + str(betting_group))
            print("To change your mind, just bet 0!")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:
                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)

    elif player_choice in io_bets[1] or player_choice in io_bets[3]:
        print("Welcome to the Outer Bets!")
        print("1. Low or High")
        print("2. Red or Black")
        print("3. Even or Odd")
        print("4. Dozen Bet")
        print("5. Column Bet")
        print("6. Snake Bet")
        while True:
            try:

                player_choice = input("Tell us your choice: :-> ").lower()
                if player_choice in o_bets[0] or player_choice in o_bets[6]:
                    break
                if player_choice in o_bets[1] or player_choice in o_bets[7]:
                    break
                if player_choice in o_bets[2] or player_choice in o_bets[8]:
                    break
                if player_choice in o_bets[3] or player_choice in o_bets[9]:
                    break
                if player_choice in o_bets[4] or player_choice in o_bets[10]:
                    break
                if player_choice in o_bets[5] or player_choice in o_bets[11]:
                    break
            except IndexError:
                print("Enter something from the list above!")
        if player_choice in o_bets[0] or player_choice in o_bets[6]:
            print("We all have our lows and highs!")
            print("Make your bet!")
            while True:
                try:
                    player_choice = input("Low or High? :-> ").lower()
                    if player_choice in "lows":
                        betting_group = [1, 2, 3, 4, 5, 6, 7, 8,
                                         9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

                        break
                    elif player_choice in "highs":
                        betting_group = [19, 20, 21, 22, 23, 24, 25,
                                         26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

                        break
                    else:
                        print("Choose from Low or High!")
                except IndexError:
                    print("Please choose from Low or High!")
            print("Your bet is on {}".format(betting_group))
            print("Just bet on 0 if you change your mind...")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:

                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)

        if player_choice in o_bets[1] or player_choice in o_bets[7]:
            print("Rouge ou Noir!")
            print("Make your bet!")
            while True:
                try:
                    player_choice = input("Red or Black? :-> ").lower()
                    if player_choice in "reds":
                        betting_group = [1, 3, 5, 7, 9, 12, 14, 16,
                                         18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

                        break
                    elif player_choice in "blacks":
                        betting_group = [2, 4, 6, 8, 10, 11, 13, 15,
                                         17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

                        break
                    else:
                        print("Choose from Red or Black!")
                except IndexError:
                    print("Please choose from Red or Black!")
            print("Your bet is on {}".format(betting_group))
            print("Just bet on 0 if you change your mind...")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:

                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)

        if player_choice in o_bets[2] or player_choice in o_bets[8]:
            print("Even out the odds!")
            print("Make your bet!")
            while True:
                try:
                    player_choice = input("Even or Odds? :-> ").lower()
                    if player_choice in "even":
                        betting_group = [2, 4, 6, 8, 10, 12, 14, 16,
                                         18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

                        break
                    elif player_choice in "odds":
                        betting_group = [1, 3, 5, 7, 9, 11, 13,
                                         15, 17, 21, 23, 25, 27, 29, 31, 33, 35]

                        break
                    else:
                        print("Choose from Even or Odds!")
                except IndexError:
                    print("Please choose from Even or Odds!")
            print("Your bet is on {}".format(betting_group))
            print("Just bet on 0 if you change your mind...")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:

                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)

        if player_choice in o_bets[3] or player_choice in o_bets[9]:
            print("Lucky by the dozen!")
            print("Make your bet!")
            while True:
                try:
                    player_choice = input(
                        "1st, 2nd or 3rd Dozen? :-> ").lower()
                    if player_choice in dozens[0] or player_choice in dozens[3]:
                        betting_group = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

                        break
                    elif player_choice in dozens[1] or player_choice in dozens[4]:
                        betting_group = [13, 14, 15, 16,
                                         17, 18, 19, 20, 21, 22, 23, 24]

                        break
                    elif player_choice in dozens[2] or player_choice in dozens[5]:
                        betting_group = [25, 26, 27, 28,
                                         29, 30, 31, 32, 33, 34, 35, 36]

                        break
                    else:
                        print("Choose from 1st, 2nd or 3rd Dozen!")
                except IndexError:
                    print("Please choose from 1st, 2nd or 3rd Dozen!")
            print("Your bet is on {}".format(betting_group))
            print("Just bet on 0 if you change your mind...")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:

                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)
        if player_choice in o_bets[4] or player_choice in o_bets[10]:
            print("Trajan's column is staring down at you!")
            print("Make your bet!")
            while True:
                try:
                    player_choice = input(
                        "1st, 2nd or 3rd Column? :-> ").lower()
                    if player_choice in dozens[0] or player_choice in dozens[3]:
                        betting_group = [
                            [n for n in range(1, 36) if n % 3 == 1]]

                        break
                    elif player_choice in dozens[1] or player_choice in dozens[4]:
                        betting_group = [
                            [n for n in range(1, 36) if n % 3 == 2]]

                        break
                    elif player_choice in dozens[2] or player_choice in dozens[5]:
                        betting_group = [
                            [n for n in range(1, 36) if n % 3 == 0]]

                        break
                    else:
                        print("Choose from 1st, 2nd or 3rd Column!")
                except IndexError:
                    print("Please choose from 1st, 2nd or 3rd Column!")
            print("Your bet is on {}".format(betting_group))
            print("Just bet on 0 if you change your mind...")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:

                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)

        if player_choice in o_bets[5] or player_choice in o_bets[11]:
            print("A snake tempts you forward!")
            print("Make your bet!")
            betting_group = [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]
            print("Your bet is on {}".format(betting_group))
            print("Just bet on 0 if you change your mind...")
            bet_amount = bet_amnt()
            lucky = choice(roulette_nums)
            print("Fortuna casts the number {}".format(lucky))
            if lucky in betting_group:

                print("If it works for you, it works for me! Congratz")
                player.money += bet_amount
            else:
                print("Daaarn! Bad luck!")
                player.money -= bet_amount
            update()
            play_again(roulette)

    choices()


os.system("cls")
title_screen()
