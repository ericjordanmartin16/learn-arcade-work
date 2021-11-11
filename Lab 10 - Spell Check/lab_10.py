import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def main():
    # Open dictionary file and load its contents into a list.
    dictionary_file = open("dictionary.txt")
    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()
        dictionary_list.append(line)

    dictionary_file.close()

    # Linear search
    print("--- Linear Search ---")
    alice_file = open("AliceInWonderLand200.txt")
    # Go through each word in the alice_file and add it to the word_list.
    line_number = 0
    for line in alice_file:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) \
                    and dictionary_list[current_list_position] != word.upper():
                current_list_position += 1

            if current_list_position == len(dictionary_list):
                print(f"Word '{word}' on line {line_number} was not found in the dictionary.")
    alice_file.close()

    # Binary search
    print("--- Binary search ---")
    alice_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in alice_file:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:

            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_position = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_position] < word.upper():
                    lower_bound = middle_position + 1
                elif dictionary_list[middle_position] > word.upper():
                    upper_bound = middle_position - 1
                else:
                    found = True

            if not found:
                print(f"Word '{word}' on line {line_number} was not found in the dictionary.")

    alice_file.close()


if __name__ == "__main__":
    main()
