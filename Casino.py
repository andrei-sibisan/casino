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
    choice = input("Make your choice, traveller! > ").lower()

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
    global player
    inp_name = input("What is your name, traveller? > ")
    player.name = inp_name
    choices()


def choices():

    global player
    greeting = "\nHello, {name}, you have travelled from far away to join our merry Casino! \nThe ocean is weary and tired tonight, so come on in and enjoy a glass of whiskey! \n\n<{name} goes inside, looking quite tired.> \n<He sips from the whiskey the waiter serves him.> \n\nOh, there you are! Garcon! His raincoat, please! Never can get enough help these days. ".format(
        name=player.name)
    print(greeting)
    print("\n\nWhat would you like to play?")
    print("1. Coin flip")
    print("2. Cha Hon")
    print("3. Roulette")
    print("4. Save Game")
    print("5. Load Game")
    print("6. Quit")
    print("\n")
    print("Current balance: " + str(player.money) + "$ ")
    choice = input("enter your choice here: >")
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
    save_name = input("Enter save game name: ").lower()

    pickle.dump(player, open("%s.sav" % save_name, "wb"))
    choices()


def load_game():
    global player
    load_name = input("Enter saved game you wish to load: ").lower()

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
    if player.money <= 0:
        print("A wing herald comes down from the ceiling, loudly proclaiming: \n" +
              quotes_dead[random_quote])
        sys.exit()


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

            if guess in str(bets[guess]) == lucky:
                player.money += int(bet)
                print(player.name + ", you have a grand total of" +
                      str(player.money) + "$!")
            else:
                player.money -= int(bet)
                print(player.name + ", you have " +
                      str(player.money) + "$ left!")
            update()

            play_again = input("Would you like to play again? ")

            if play_again in play_again_list[0]:
                coin_flip()
            elif play_again in play_again_list[1]:
                choices()
            else:
                print("Enter a valid choice!")
                play_again()
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
            input("What amount are you wagering on this most simple card game? $$$ "))
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

        print("The enemy card is: {}".format(card_dict[enemy_card]))

        if player_card > enemy_card:
            player.money += bet
            print("Wow, you have won {} $!".format(bet))
        else:
            player.money -= bet
            print("Sadly you have lost {} $. Better luck next time!".format(bet))

        update()
        play_again(function)

    choices()


def play_again(function):

    while True:
        play_again_str = input("Would you like to play again? ")
        if play_again_str in play_again_list[0] or play_again_str in play_again_list[1]:
            break
    if play_again_str in play_again_list[0]:
        function()
    elif play_again_str in play_again_list[1]:
        choices()


def roulette():
    print("Playing roulette")
    choices()


os.system("clear")
title_screen()
