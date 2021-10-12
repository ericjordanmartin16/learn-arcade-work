class Room:
    def __init__(self,
                 description: str = "",
                 north: int = 0,
                 east: int = 0,
                 south: int = 0,
                 west: int = 0
                 ):
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west


def main():
    room_list = []
    current_room = 0

    # Set initial properties to each of the rooms.
    # Room 0
    room = Room("You are currently in the dining room. You can move north or east.", 3, 1, None, None)
    room_list.append(room)

    # Room 1
    room = Room("You are currently in the kitchen. You can move north, east, or west.", 4, 2, None, 0)
    room_list.append(room)

    # Room 2
    room = Room("You are currently in the living room. You can move north or west.", 5, None, None, 1)
    room_list.append(room)

    # Room 3
    room = Room("You are currently in the bathroom. You can move south or east.", None, 4, 0, None)
    room_list.append(room)

    # Room 4
    room = Room("You are currently in the bedroom. You can move south, east, or west.", None, 5, 1, 3)
    room_list.append(room)

    # Room 5
    room = Room("You are currently in the laundry room. You can move south or west.", None, None, 2, 4)
    room_list.append(room)

    # Print introductory material
    print("You are trapped in a building with only 6 rooms! "
          "Your job is to move around from room to room until you get bored.")
    print("There\'s no escape; sorry!")
    done = False
    while not done:
        print()
        print("Press Q to quit the game")
        print(room_list[current_room].description)
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
