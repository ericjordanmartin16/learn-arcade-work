def give_money1(person):
    person.money += 100


class Person:
    def __init__(self):
        self.name = ""
        self.money = 0


def main():
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    give_money1(bob)
    print(bob.money)
    # line 2 variable 'money' is different than line 8 attribute 'money'

    nancy = bob
    nancy.name = "Nancy"

    print(bob.name, "has", bob.money, "dollars.")
    print(nancy.name, "has", nancy.money, "dollars.")


main()
