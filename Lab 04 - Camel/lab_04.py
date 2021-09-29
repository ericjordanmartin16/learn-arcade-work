# Lab 04 - Camel Lab. Eric Martin, Intro to Programming. Instructor Paul Craven.
# 23 September 2021

import random


def print_intro():
    print("""Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives.""")


def main():
    print_intro()

    my_travel_distance = 0
    my_thirst = 0
    camel_tiredness = 0
    natives_travel_distance = -20
    drinks_in_canteen = 3

    done = False
    while not done:
        print("")
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print("")

        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            # quit the game.
            done = True
            print("You have quit the game.")
        elif user_choice.upper() == "E":
            # status check.
            print("Miles traveled:", my_travel_distance)
            print("Drinks in canteen:", drinks_in_canteen)
            natives_travel_behind_you = my_travel_distance - natives_travel_distance
            print("The natives are", natives_travel_behind_you, "miles behind you.")
        elif user_choice.upper() == "D":
            # stop for the night.
            camel_tiredness = 0
            print("Your camel is happy.")
            natives_travel_distance += random.randrange(7, 14)
        elif user_choice.upper() == "C":
            # ahead full speed.
            full_speed_travel_distance = random.randrange(10, 21)
            my_travel_distance += full_speed_travel_distance
            print("You traveled", full_speed_travel_distance, "miles at full speed.")
            print("You have traveled", my_travel_distance, "miles in total.")
            my_thirst += 1
            camel_tiredness += 1
            natives_travel_distance += random.randrange(7, 14)
        elif user_choice.upper() == "B":
            # ahead moderate speed.
            moderate_speed_travel_distance = random.randrange(5, 13)
            my_travel_distance += moderate_speed_travel_distance
            print("You traveled", moderate_speed_travel_distance, "miles at moderate speed.")
            print("You have traveled", my_travel_distance, "miles in total.")
            my_thirst += 1
            camel_tiredness += 1
            natives_travel_distance += random.randrange(7, 14)
        elif user_choice.upper() == "A":
            # drink from canteen
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
            else:
                print("You have no more drinks left in the canteen!")
        else:
            print("You entered an invalid character. Please try again.")




main()