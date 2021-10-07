class Dog():
    def __init__(self, name):
        """ Constructor """
        self.name = name
        print("A dog has been born!")


def main():
    # This creates the dog
    my_dog = Dog("Spot")
    print(f"The dog's name is: {my_dog.name}")

    # This creates the dog
    my_other_dog = Dog("Sam")
    print(f"The dog's name is: {my_other_dog.name}")


main()