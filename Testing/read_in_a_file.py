def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")
    villain_list = []

    # Loop through each line in the file like a list
    # line includes the character return!
    for line in my_file:
        # This command removes the character return at the end.
        line = line.strip()
        villain_list.append(line)

    # Always do this when you are finished using the file.
    my_file.close()

    print(villain_list)
    print("There were", len(villain_list), "names in the file.")

    key = "Octavia the Siren"

    # Linear search
    current_list_position = 0
    # The order matters in the conditions of the while loop!
    while current_list_position < len(villain_list) and villain_list[current_list_position] != key:
        current_list_position += 1

    """if current_list_position == len(villain_list):
        print("Not found.")"""

    if current_list_position > len(villain_list):
        print("Found at:", current_list_position)
    else:
        print("Not found.")

    # Binary search
    lower_bound = 0
    upper_bound = len(villain_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_position = (lower_bound + upper_bound) // 2

        if villain_list[middle_position] < key:
            lower_bound = middle_position + 1
        elif villain_list[middle_position] > key:
            upper_bound = middle_position - 1
        else:
            found = True

    if found:
        print("Found at position:", middle_position)

    if not found:
        print("Not found.")


"""def with_main():
     Read in lines from a file 
    # Newer, more modern way to do it!

    # Open file, and automatically close when we exit this block.
    with open("super_villains.txt") as my_file:

        # Loop through each line in the file like a list
        for line in my_file:
            line = line.strip()
            print(line)"""


main()
