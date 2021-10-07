class Address:
    """ Hold all the fields for a mailing address. """
    def __init__(self, line1, line2, city, state, zip, country):
        """ Set up the address fields. """
        self.name = ""
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country


def print_address(address):
    """ Print an address to the screen """

    print(address.name)
    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print(address.line2)
    print(address.city + ", " + address.state + " " + address.zip)


def main():
    my_address = Address("701 N. C Street",
                         "Carver Science Building",
                         "Indianola",
                         "IA",
                         "50125",
                         "USA")
    # Create an address
    home_address = Address()

    # Set the fields in the address
    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

    # Create another address
    vacation_home_address = Address()

    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in " + home_address.city)
    print("His vacation home is in " + vacation_home_address.city)


main()

"""name = "Link"
outfit = "Green"
max_hit_points = 50
current_hit_points = 50
armor_amount = 6
max_speed = 10


def display_character(name, outfit, max_hit_points, current_hit_points, armor, max_speed):
    print(name, outfit, max_hit_points, current_hit_points)"""