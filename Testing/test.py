"""temperature = 5
print(temperature)"""

"""
x = 3
y = 2 * x
z = x * (3 + x)
print(z)
"""
def print_number(my_number):
    """
    This function prints hello.
    """
    print(my_number)

def add_number(a, b):
    """
    This function prints hello.
    """
    print(a + b)

def sum_two_numbers(a, b):
    result = a + b
    return result

def volume_cylinder(radius, height):
    PI = 3.141596
    volume = PI * radius ** 2 * height
    return volume



def print_hello():
    """
    This function prints hello.
    """
    print("Hello!")


def print_goodbye():
    """
    This function prints goodbye.
    """
    print("Goodbye!")


def main():
    my_result = sum_two_numbers(5, 6)
    print(my_result)

    my_volume = volume_cylinder(2.5, 5) * 6
    print(my_volume)


    print_hello()
    print_goodbye()
    print_number(5)
    print_number(6)
    print_number(22)
    add_number(11, 7)
    sum_two_numbers(5, 6)

# If imported into another program, will not run the program, only imports the functions.
if __name__ == "__main__":
    main()