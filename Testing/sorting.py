# Sorting

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
print(my_list)

# Swap the 15 and 14 values w/o assuming their values.
temp = my_list[2]
my_list[2] = my_list[0]
my_list[0] = temp

print(my_list)

# *********************This is the SELECTION sort. I am SELECTING the smallest value and swapping.

# 37 18 99 30 82 5 41

# Go through the list, checking each number to the 0th number. If less than the 0th, number, swap
# positions with the 0th number.

# Start
# 15 57 14 33 72 79 26 56 42 40

# 14 is smallest, swap 14 to pos 0.
# 14 57 15 33 72 79 26 56 42 40

# 15 is next smallest, swap 15 to pos 1.
# 14 15 57 33 72 79 26 56 42 40

# 26 is next smallest, swap 26 to pos 2.
# 14 15 26 33 72 79 57 56 42 40

# 33 is next smallest, swap 33 to pos 3.
# 14 15 26 33 72 79 57 56 42 40

# 40 is next smallest, swap 40 to pos 4.
# 14 15 26 33 40 79 57 56 42 72

# *********************This is the SELECTION sort. I am SELECTING the smallest value and swapping.


def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)): # If we have 100 elements, this loop will run 99 times. (or 100)
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # Worst - 50, Avg. - 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)

# Selection sort, all cases
# Loops:  outside num_times * inside num_times = product
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2  <---  How many times we expect this to run

# Don't use 'Big O' notation.

# Insertion sort, worst case
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2  <---  How many times we expect this to run

# Insertion sort, average case
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 14 = 2500
# n = 1000, 1000 * 250 = 250,000
# n * (n / 4) = n^2 / 4  <---  How many times we expect this to run

# Insertion sort,
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1000
# n  <---  How many times we expect this to run