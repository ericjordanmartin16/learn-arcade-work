"""for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1"""

import random

my_number = random.randrange(5)
if my_number == 0:
    print("Dragon!")
else:
    print("No dragon.")
print(my_number)

my_other_number = random.random()
print(my_other_number * 9 + 1)


# Write a function called count_up that takes in two numbers.
# Prints all the numbers from start to finish, inclusive.
# Test with 5, 10
"""def count_up(start, end):
    for number in range(start, end + 1):
        print(number)


count_up(5, 10)

done = False"""

"""while not done:
    quit = input("Do you want to quit? ")
    if quit.lower == "y":
        done = True
        print("Bye!")
        continue

    attack = input("Do you want to attack the dragon? ")
    if attack.lower() == "y":
        done = True
        print("Bad choice, you died!")"""





"""quit = "n"
while quit.lower() == "n" or quit.lower() == "no":
    quit = input("Do you want to quit? ")"""