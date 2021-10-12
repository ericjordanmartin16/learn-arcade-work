class Dog:
    def __init__(self):
        """ Constructor """
        self.age = 0
        self.name = ""
        self.weight = 0

    # Function in a class is called a 'method'
    def bark(self):
        if self.weight < 10:
            print("Yip! says", self.name)
        else:
            print("Woof! says", self.name)


def main():
    # This creates the dog
    my_dog = Dog()
    my_dog.name = "Spot"
    my_dog.weight = 20
    my_dog.age = 3

    my_other_dog = Dog()
    my_other_dog.name = "Fluffy"
    my_other_dog.weight = 9
    my_other_dog.age = 3

    my_dog.bark()
    my_other_dog.bark()


main()