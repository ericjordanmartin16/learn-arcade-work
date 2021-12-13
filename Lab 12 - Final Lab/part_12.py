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
        if room_list[current_room].room_number == item.room_number:
            # print(f"room_list[current_room].room_number = {room_list[current_room].room_number}")
            # print(f"item.room_number = {item.room_number}")
            return item.description
    return "There are no items in the room."


def main():
    room_list = []
    item_list = []
    current_room = 0

    # Set initial properties to each of the rooms.
    # Room 0
    """
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

    for room in room_list:
        north = room.room_number + 3
        south = room.room_number - 3
        east = room.room_number + 1
        west = room.room_number - 1

    spoon = Item(1, "There is a spoon sitting on the counter top.", "spoon")
    item_list.append(spoon)

    armchair = Item(2, "There is an armchair sitting on the floor.", "armchair")
    item_list.append(armchair)

    soap = Item(3, "There is a bar of soap sitting near the sink.", "soap")
    item_list.append(soap)"""

    # Load the Room and Item objects from the Room_Item_values.txt file
    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    values_file = open("Room_Item_values.txt")

    # Loop through each line in the file like a list
    # line includes the character return!
    for line in values_file:
        # This command removes the character return at the end.
        line = line.strip()
        # print(line)
        splits = line.split('|')
        # print(splits)
        counter = 0
        object_type = ""
        room_room_number = 0
        room_description = ""
        item_room_number = 0
        item_description = ""
        name = ""
        north = 0
        east = 0
        south = 0
        west = 0
        string_count = len(splits)

        if string_count == 7:
            # if string_count == 7, this means that this is a Room object.
            for split in splits:
                if counter == 0:
                    object_type = split
                    # print(object_type)
                elif counter == 1:
                    room_room_number = int(split)
                    # print(room_room_number)
                elif counter == 2:
                    room_description = split
                    # print(room_description)
                elif counter == 3:
                    north = int(split)
                    # print(north)
                elif counter == 4:
                    east = int(split)
                    # print(east)
                elif counter == 5:
                    south = int(split)
                    # print(south)
                elif counter == 6:
                    west = int(split)
                    # print(west)
                counter += 1
            room = Room(room_room_number, room_description, north, east, south, west)
            room_list.append(room)
        elif string_count == 4:
            # if string_count == 4, this means that this is a Item object.
            for split in splits:
                if counter == 0:
                    object_type = split
                if counter == 1:
                    item_room_number = int(split)
                if counter == 2:
                    item_description = split
                if counter == 3:
                    name = split
                counter += 1
            item = Item(item_room_number, item_description, name)
            item_list.append(item)

    values_file.close()

    # Print introductory material
    print("You are trapped in a building with only 6 rooms! "
          "Your job is to move around from room to room until you get bored.")
    print("There\'s no escape; sorry!")
    done = False
    while not done:
        print()
        print("Press Q to quit the game")
        """print(room_list)
        print(item_list)
        print(room_list[current_room])
        print(room_list[current_room].north)
        print(room_list[current_room].east)
        print(room_list[current_room].south)
        print(room_list[current_room].room_number)"""
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
            if next_room == 9:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "s" or command_words[0].lower() == "south":
            next_room = room_list[current_room].south
            if next_room == 9:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "e" or command_words[0].lower() == "east":
            next_room = room_list[current_room].east
            if next_room == 9:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "w" or command_words[0].lower() == "west":
            next_room = room_list[current_room].west
            if next_room == 9:
                print("There is no passageway in that direction. Please try again.")
            else:
                current_room = next_room
        elif command_words[0].lower() == "q":
            confirm_quit = input("Are you sure you want to quit? ")
            if confirm_quit.lower() == "y" or confirm_quit.lower() == "yes":
                done = True

        elif command_words[0].lower() == "get":
            if len(command_words) == 1:
                print("Please specify item to get.")
                continue
            item_to_get = command_words[1]
            item_found = False
            for item in item_list:
                if item.name == item_to_get:
                    if item.room_number == current_room:
                        print(f"Item '{item.name}' has been picked up.")
                        item.room_number = -1
                        item_found = True
                    else:
                        print(f"Item '{item.name}' is not found in the current room.")
                        item_found = True
            if not item_found:
                print(f"Item '{command_words[1]}' is not even in the game!")

        elif command_words[0].lower() == "inventory":
            print("Here are the items that you have collected so far:")
            for item in item_list:
                if item.room_number == -1:
                    print(item.name)

        elif command_words[0].lower() == "drop":
            if len(command_words) == 1:
                print("Please specify item to drop.")
                continue
            item_to_get = command_words[1]
            item_found = False
            for item in item_list:
                if item.name == item_to_get:
                    if item.room_number == -1:
                        print(f"Item '{item.name}' has been dropped off.")
                        item.room_number = room_list[current_room].room_number
                        item_found = True
                    elif item.room_number == -2:
                        print(f"Item '{item.name}' has already been used and cannot be dropped.")
                        item_found = True
                    else:
                        print(f"Item '{item.name}' cannot be dropped off until it has been picked up.")
                        item_found = True
            if not item_found:
                print(f"Item '{command_words[1]}' is not even in the game!")

        elif command_words[0].lower() == "use":
            if len(command_words) == 1:
                print("Please specify item to use.")
                continue
            item_to_get = command_words[1]
            item_found = False
            for item in item_list:
                if item.name == item_to_get:
                    if item.room_number == -1:
                        print(f"Item '{item.name}' has been used. It cannot be used again.")
                        if item.name == "fork":
                            print("Congratulations!! Now you get to use the fork to eat a big piece of chocolate cake!")
                        if item.name == "spoon":
                            print("Congratulations!! Now you get to use the spoon to eat a big bowl of ice cream!")
                        if item.name == "armchair":
                            print("Congratulations!! Now you get to sit in the armchair and take a nice, long nap!")
                        if item.name == "soap":
                            print("Congratulations!! Now you have nice, clean hands!")
                        item.room_number = -2
                        item_found = True
                    elif item.room_number == -2:
                        print(f"Item '{item.name}' has already been used and cannot be used again.")
                        item_found = True
                    else:
                        print(f"Item '{item.name}' cannot be used until it has been picked up.")
                        item_found = True
            if not item_found:
                print(f"Item '{command_words[1]}' is not even in the game!")

        else:
            print("You entered an invalid command. Please try again.")


main()
