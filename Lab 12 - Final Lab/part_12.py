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
    """
    Function that takes in the current room as a parameter (as well as
    the room and item lists) and returns the descriptions of the items in
    that particular room.
    """
    for item in item_list:
        item.room_number == room_list[current_room].room_number
        # if room_list[current_room].room_number == item.room_number:
        current_room_string = f"room_list[current_room].room_number = {room_list[current_room].room_number}"
        item_room_string = f"item.room_number = {item.room_number}"
        return current_room_string, item_room_string, item.description

        # else:
            # return "There are no items in the room."


def main():
    room_list = []
    item_list = []
    current_room = 0
    current_item_in_room = 0

    # Set initial properties to each of the rooms.
    # Room 0
    room = Room(0, "You are currently in the dining room. You can move north or "
                   "east.", 3, 1, None, None)
    room_list.append(room)

    # Room 1
    room = Room(1, "You are currently in the kitchen. You can move north, east, "
                   "or west.", 4, 2, None, 0)
    room_list.append(room)

    # Room 2
    room = Room(2, "You are currently in the living room. You can move north or "
                   "west.", 5, None, None, 1)
    room_list.append(room)

    # Room 3
    room = Room(3, "You are currently in the bathroom. You can move south or "
                   "east.", None, 4, 0, None)
    room_list.append(room)

    # Room 4
    room = Room(4, "You are currently in the bedroom. You can move south, east, "
                   "or west.", None, 5, 1, 3)
    room_list.append(room)

    # Room 5
    room = Room(5, "You are currently in the laundry room. You can move south or "
                   "west.", None, None, 2, 4)
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

        # Asks the user for a command and enters the user's input into a list, each word being a
        # different element.
        user_input = input("What is your command? ")
        command_words = user_input.split(" ")

        # Code to display the description of the next room based on the input of the user.
        if command_words[0].lower() == "n" or command_words[0].lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "s" or command_words[0].lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "e" or command_words[0].lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "w" or command_words[0].lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "q":
            confirm_quit = input("Are you sure you want to quit? ")
            if confirm_quit.lower() == "y" or confirm_quit.lower() == "yes":
                done = True

        elif command_words[0].lower() == "get":
            print(f"Current room: {room_list[current_room].room_number}")
            item_found = False
            for word in command_words:
                for item in item_list:
                    current_list_position = 0
                    while current_list_position < len(command_words) \
                            and command_words[current_list_position] != word \
                            and not item_found:
                        current_list_position += 1
                        if item.room_number == current_room and item.name == command_words[1]:
                            print(f"Item '{item.name}' has been picked up.")
                            item.room_number = -1
                            print(f"item.room_number is now equal to {item.room_number}")
                            item_found = True
                        elif item.room_number != current_room and item.name == command_words[1]:
                            print(f"Item '{item.name}' is not found in the current room.")
                            item_found = True
                        elif command_words[1] != item:
                            print(f"Item '{command_words[1]}' is not even in the game!")
                            item_found = True
            print(f"Spoon is in room {spoon.room_number}")
            print(f"Armchair is in room {armchair.room_number}")
            print(f"Soap is in room {soap.room_number}")

        else:
            print("You entered an invalid character. Please try again.")


main()
