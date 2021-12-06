class Room:
    def __init__(self,
                 room_number: int = 0,
                 description: str = "",
                 north: int = 0,
                 east: int = 0,
                 south: int = 0,
                 west: int = 0
                 ):
        self.room_number: int = room_number
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west


class Item:
    def __init__(self,
                 room_number: int = 0,
                 description: str = "",
                 name: str = ""
                 ):
        self.room_number: int = room_number
        self.description: str = description
        self.name: str = name


def fetch_items_in_room(room_list, current_room, item_list):
    for item in item_list:
        if room_list[current_room].room_number == item.room_number:
            return item.description
        else:
            return "There are no items in the room"


def main():
    room_list = []
    item_list = []
    current_room = 0
    current_item_in_room = 0

    # Set initial properties to each of the rooms.
    # Room 0
    room = Room(0, "You are currently in the dining room. You can move north or east.", 3, 1, None, None)
    room_list.append(room)

    # Room 1
    room = Room(1, "You are currently in the kitchen. You can move north, east, or west.", 4, 2, None, 0)
    room_list.append(room)

    # Room 2
    room = Room(2, "You are currently in the living room. You can move north or west.", 5, None, None, 1)
    room_list.append(room)

    # Room 3
    room = Room(3, "You are currently in the bathroom. You can move south or east.", None, 4, 0, None)
    room_list.append(room)

    # Room 4
    room = Room(4, "You are currently in the bedroom. You can move south, east, or west.", None, 5, 1, 3)
    room_list.append(room)

    # Room 5
    room = Room(5, "You are currently in the laundry room. You can move south or west.", None, None, 2, 4)
    room_list.append(room)

    spoon = Item(1, "There is a spoon sitting on the counter top.", "spoon")
    item_list.append(spoon)

    armchair = Item(2, "There is an armchair sitting on the floor.", "armchair")
    item_list.append(armchair)

    soap = Item(3, "There is a bar of soap sitting near the sink.", "soap")
    item_list.append(soap)

    # Print introductory material
    print("You are trapped in a building with only 6 rooms! "
          "Your job is to move around from room to room until you get bored.")
    print("There\'s no escape; sorry!")
    done = False
    while not done:
        print()
        print("Press Q to quit the game")
        print(room_list[current_room].description)
        item_description = fetch_items_in_room(room_list, current_room, item_list)
        print(item_description)
        user_input = input("Which direction do you want to go? ")

        # Code to display the description of the next room based on the input of the user.
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif user_input.lower() == "q":
            confirm_quit = input("Are you sure you want to quit? ")
            if confirm_quit.lower() == "y" or confirm_quit.lower() == "yes":
                done = True
        else:
            print("You entered an invalid character. Please try again.")


main()
